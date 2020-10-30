import celery
from celery import Celery
import celery_pubsub

worker = Celery('cpe', broker='redis://redis:6379/0')

@celery.task
def my_task_1(*args, **kwargs):
    return "task 1 done"

celery_pubsub.subscribe('some.topic', my_task_1)
