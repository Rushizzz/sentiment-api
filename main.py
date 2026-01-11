from fastapi import FastAPI 
from transformers import pipeline
from pydantic import BaseModel
import os

# for sql
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

# Load the sentiment analysis model
model_path = "./model_directory"
classifier = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)

class SentimentRequest(BaseModel):
    text: str

# Create database connection 
# DATABASE_URL = "sqlite:///./sentiment.db"

# env var first one not found then use second
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sentiment.db")

# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# 1. Define the connection arguments based on the database type
connect_args = {}

# Only use "check_same_thread" if we are actually using SQLite
if "sqlite" in DATABASE_URL:
    connect_args = {"check_same_thread": False}

# 2. Create the engine with the dynamic arguments
engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args
)

# Create a session factory (to talk to DB)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base class for our table
Base = declarative_base()

# define our table 
class PredictionLog(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    label = Column(String)
    score = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

# create the table in database
Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello AI"}

@app.post("/predict")
def predict(request: SentimentRequest):
    # We access the data using request.text
    ai_result = classifier(request.text)
    
    #prepare data for DB
    db_entry = PredictionLog(
        text=request.text,
        label=ai_result[0]['label'],
        score=ai_result[0]['score']
    )

    # save to db
    db = SessionLocal()     # open connection
    try:
        db.add(db_entry) # add to staging
        db.commit()      # save changes
        db.refresh(db_entry) # get the generated id
    finally:
        db.close()  # close the connection (Very important)
    
    return ai_result

