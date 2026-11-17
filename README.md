# Student Course API

A beginner-friendly, read-only REST API built with Python and Flask for the System Integration and Architecture lesson.

## Features
- `GET /api/health` — checks whether the service is running.
- `GET /api/courses` — returns six fictional courses.
- `GET /api/courses/1` — returns the course with ID 1.
- `GET /api/courses/9999` — returns HTTP 404 with a JSON error.

## Run locally
1. Install Python 3.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the server:
   ```bash
   python app.py
   ```
4. Open `http://127.0.0.1:5000/api/health`.

## Render deployment
- Service type: Web Service
- Runtime: Python 3
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`

The `app:app` command means the Flask variable `app` is in the Python file `app.py`.

## Important notes
- This project uses fictional sample data only.
- It does not connect to a database and does not store real student records.
- It is a learning prototype, not a complete student information system.
- CORS is open for classroom testing. Restrict allowed origins before production use.
