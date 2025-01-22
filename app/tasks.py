from celery import Celery
import time

# Setup Celery to use RabbitMQ as the broker
celery_app = Celery('tasks', broker='pyamqp://guest:guest@rabbitmq//')

@celery_app.task
def create_task(task: str):
    time.sleep(5)  # Simulate a time-consuming task
    return f"Task {task} completed"
