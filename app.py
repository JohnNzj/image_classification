from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io
from model import predict

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Hugging Face Image Classification API"}

@app.post("/predict/")
async def classify_image(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))  # Read the uploaded image
    prediction = predict(image)  # Get model prediction
    return {"prediction": prediction}
