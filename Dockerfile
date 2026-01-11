FROM python:3.9 

WORKDIR /app 

COPY requirements.txt .

# install libraries
RUN pip install -r requirements.txt 

# copy loader script
COPY model_loader.py .

# run the loader script to download and save the model
RUN python model_loader.py

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

