import time

from celery import shared_task


@shared_task
def create_tasks(a, b):
    time.sleep(2)
    return a + b
