from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine
from routers import tasks, auth

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TaskTracker API",
    description="A secure and robust RESTful API for managing daily tasks and productivity.",
    version="2.0.0"
)

# Configure CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production environments
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Welcome to the TaskTracker API. Visit /docs for the interactive Swagger UI."}
