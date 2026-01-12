# Sentiment Analysis API

A FastAPI-based sentiment analysis service that uses Hugging Face's transformers library to analyze text sentiment and stores predictions in a database.

## 🚀 Live Deployment

This API is deployed and running on **[Render.com](https://render.com)**

- **Live API URL**: [https://sentiment-app-v1-7czw.onrender.com/](https://sentiment-app-v1-7czw.onrender.com/)
- **Status**: Production Ready

## 🛠 Tech Stack

- **Web Framework**: FastAPI
- **Server**: Uvicorn
- **AI/ML**: Transformers (by Hugging Face)
- **Model**: DistilBERT-base-uncased-finetuned-sst-2-english
- **Database**: SQLite (local) / PostgreSQL (production)
- **ORM**: SQLAlchemy
- **Containerization**: Docker

## 📋 Features

- Sentiment analysis using pre-trained BERT model
- RESTful API endpoints
- Database logging of all predictions
- Docker support for easy deployment
- Environment-based database configuration

## 🔧 Installation & Setup

### Local Development

1. Clone the repository:
```bash
git clone <repository-url>
cd sentiment-api
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download the model:
```bash
python model_loader.py
```

5. Run the application:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## 🐳 Docker Deployment

### Build Image
```bash
docker build -t sentiment-app .
```

### Run Container
```bash
docker run -p 8000:8000 \
    -v $(pwd)/sentiment.db:/app/sentiment.db \
    sentiment-app
```

### Using Docker Compose
```bash
docker-compose up --build
```

## 📡 API Endpoints

### Home
- **GET** `/`
- Returns: `{"message": "Hello AI"}`

### Predict Sentiment
- **POST** `/predict`
- Request Body:
```json
{
    "text": "Your text here"
}
```
- Returns:
```json
[
    {
        "label": "POSITIVE" | "NEGATIVE",
        "score": 0.9998
    }
]
```

## 🗄 Database Configuration

The application supports both SQLite and PostgreSQL databases:

- **Local Development**: Uses SQLite (`sentiment.db`)
- **Production**: Uses PostgreSQL via `DATABASE_URL` environment variable

### Database Schema
The `predictions` table stores:
- `id`: Primary key
- `text`: Input text
- `label`: Predicted sentiment (POSITIVE/NEGATIVE)
- `score`: Confidence score
- `timestamp`: Prediction timestamp

## 🔒 Environment Variables

- `DATABASE_URL`: Database connection string (optional, defaults to SQLite)
  - SQLite: `sqlite:///./sentiment.db`
  - PostgreSQL: `postgresql://user:password@host:port/database`

## 📊 Model Information

- **Model**: `distilbert-base-uncased-finetuned-sst-2-english`
- **Type**: Sentiment Analysis
- **Labels**: POSITIVE, NEGATIVE
- **Framework**: Hugging Face Transformers

## 🚀 Deployment on Render.com

1. Connect your GitHub repository to Render.com
2. Create a new Web Service
3. Set the following environment variables:
   - `DATABASE_URL`: Your PostgreSQL connection string (if using external DB)
4. Render will automatically build and deploy your Docker container
5. Your API will be available at the provided Render URL

## 📝 Usage Example

```python
import requests

# Test the API
response = requests.post(
    "https://your-app.onrender.com/predict",
    json={"text": "I love this product!"}
)

result = response.json()
print(f"Sentiment: {result[0]['label']}")
print(f"Score: {result[0]['score']}")
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.



