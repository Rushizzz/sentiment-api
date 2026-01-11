# sentiment-api

## Tech stack 

- Web Framework: Fast API
- Server: Uvicorn
- AI library: transformers (by Hugging Face)


## Docker commands

### Build image
```bash
docker build -t sentiment-app .
```

### Run container
```bash
docker run -p 8000:8000 \
    -v $(pwd)/sentiment.db:/app/sentiment.db \
    sentiment-app
```



