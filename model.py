from transformers import AutoModelForImageClassification, AutoFeatureExtractor
import torch
from PIL import Image

# Load model and feature extractor
MODEL_NAME = "facebook/deit-tiny-patch16-224"
model = AutoModelForImageClassification.from_pretrained(MODEL_NAME)
feature_extractor = AutoFeatureExtractor.from_pretrained(MODEL_NAME)
model.eval()  # Set model to evaluation mode

def predict(image: Image.Image):
    """Preprocess image and return predicted label."""
    inputs = feature_extractor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        predicted_idx = torch.argmax(outputs.logits, dim=-1).item()
    
    return model.config.id2label[predicted_idx]  # Get class label
