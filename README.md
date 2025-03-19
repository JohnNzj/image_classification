# image_classification with docker and fastapi

docker build -t ml_vision .  
docker run -p 8000:8000 ml_vision  
curl -X POST "http://127.0.0.1:8000/predict/" -F "file=@test.jpg"  
