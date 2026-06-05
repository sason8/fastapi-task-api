from fastapi import FastAPI
import models
from database import engine
from routers import tasks

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TaskTracker API",
    description="A robust RESTful API for managing daily tasks and productivity.",
    version="1.0.0"
)

app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Welcome to the TaskTracker API. Visit /docs for the Swagger UI."}
