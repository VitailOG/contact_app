backend:
	uvicorn src.main:app --reload

worker:
	celery -A src.celery worker --loglevel=info

beat:
	celery -A src.celery beat --loglevel=info
