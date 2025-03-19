# image_classification with docker and fastapi

# To run with docker:  
docker build -t ml_vision .  
docker run -p 8000:8000 ml_vision  
curl -X POST "http://127.0.0.1:8000/predict/" -F "file=@test.jpg"  

# To run locally:  
uvicorn app:app --host 0.0.0.0 --port 8000 --reload  
curl -X POST "http://127.0.0.1:8000/predict/" -F "file=@test.jpg"
