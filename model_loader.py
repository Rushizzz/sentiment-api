from transformers import pipeline

print("Downloading model")
#this downloads the default sentiment-analysis model
pipe = pipeline("sentiment-analysis",model="distilbert-base-uncased-finetuned-sst-2-english")

# Save it locally to folder named 'model_directory'
print("Saving Model to ./model_directory")
pipe.save_pretrained("./model_directory")

print("Model saved")