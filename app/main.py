from fastapi import FastAPI
from app.tasks import create_task

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI with Celery!"}

@app.post("/create-task/")
async def create_new_task(task: str):
    task_id = create_task.delay(task)
    return {"task_id": task_id}
