# 📝 TaskTracker API

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

A high-performance RESTful API built with **FastAPI** for managing tasks. It utilizes **SQLAlchemy** as an ORM and features interactive API documentation via Swagger UI.

## Architecture
- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Data Validation**: Pydantic v2
- **Database**: SQLite (easy to swap to PostgreSQL)

## Setup & Installation

1. Clone the repository and navigate to the directory.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the development server:
   ```bash
   uvicorn main:app --reload
   ```

## API Documentation
Once the server is running, visit `http://localhost:8000/docs` to access the interactive Swagger UI and test the endpoints directly from your browser.
