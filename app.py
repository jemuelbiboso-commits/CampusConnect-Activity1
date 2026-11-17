from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# Classroom demonstration: allow cross-origin requests.
# Restrict this to known frontend origins for a real deployment.
CORS(app)

courses = [
    {"id": 1, "code": "ITAS 3228", "name": "Web and Mobile Development",
     "description": "Introduction to web and mobile applications."},
    {"id": 2, "code": "ITAS 3229", "name": "System Integration and Architecture",
     "description": "How software components communicate and work together."},
    {"id": 3, "code": "ITAS 3230", "name": "Database Management",
     "description": "Fundamentals of organizing and managing data."},
    {"id": 4, "code": "ITAS 3231", "name": "Programming Fundamentals",
     "description": "Basic programming concepts and problem solving."},
    {"id": 5, "code": "ITAS 3232", "name": "Networking Fundamentals",
     "description": "Introduction to computer networks and communication."},
    {"id": 6, "code": "ITAS 3233", "name": "Information Assurance",
     "description": "Basic concepts of information security and privacy."}
]

@app.get("/")
def home():
    return jsonify({
        "message": "Welcome to the Student Course API",
        "endpoints": ["/api/health", "/api/courses", "/api/courses/1"]
    }), 200

@app.get("/api/health")
def health():
    return jsonify({"status": "healthy", "message": "Student Course API is running"}), 200

@app.get("/api/courses")
def get_courses():
    return jsonify(courses), 200

@app.get("/api/courses/<int:course_id>")
def get_course(course_id):
    course = next((item for item in courses if item["id"] == course_id), None)
    if course is None:
        return jsonify({"error": "Course not found", "course_id": course_id}), 404
    return jsonify(course), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
