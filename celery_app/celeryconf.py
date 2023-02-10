from celery import Celery
from app.core.settings import settings

celery = Celery(
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_BROKER_URL
)
celery.autodiscover_tasks([
    'celer.tasks'
])
