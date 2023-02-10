# Fastapi python

--- 
Requirements:
- python 3.7+
---

## Start project
### Run for dev
```
python3 -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
uvicorn main:app --reload --port 8008 
```
- Run worker
```
celery -A celery_app.celeryconf worker --loglevel=info
```
- Run beat
```
celery -A celery_app.celeryconf beat --loglevel=info
```
### Run docker
```
docker-compose up --build -d
```