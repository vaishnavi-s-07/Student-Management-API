from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
import sqlite3
import secrets
import os

app = FastAPI(title="Student Management API")

security = HTTPBasic()

# Database Setup
def init_db():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        course TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

init_db()

# Student Model
class Student(BaseModel):
    name: str
    email: str
    course: str

# Home API
@app.get("/")
def home():
    return {
        "message": "Student Management API is Running Successfully!"
    }

# GET - View Students
@app.get("/students")
def get_students():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    conn.close()

    return {"students": data}

# POST - Add Student
@app.post("/students")
def create_student(student: Student):
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
        (student.name, student.email, student.course)
    )

    conn.commit()
    student_id = cursor.lastrowid
    conn.close()

    return {
        "message": "Student Created Successfully!",
        "student_id": student_id
    }

# PUT - Update Student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET name=?, email=?, course=? WHERE id=?",
        (student.name, student.email, student.course, student_id)
    )

    conn.commit()
    updated = cursor.rowcount
    conn.close()

    if updated == 0:
        return {"message": "Student Not Found"}

    return {"message": "Student Updated Successfully!"}

# DELETE - Delete Student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()
    deleted = cursor.rowcount
    conn.close()

    if deleted == 0:
        return {"message": "Student Not Found"}

    return {"message": "Student Deleted Successfully!"}

# Basic Authentication
@app.get("/secure")
def secure_api(credentials: HTTPBasicCredentials = Depends(security)):

    username = os.getenv("API_USERNAME")
    password = os.getenv("API_PASSWORD")

    if not username or not password:
        raise HTTPException(
            status_code=503,
            detail="Authentication is not configured"
        )

    if not (
        secrets.compare_digest(credentials.username, username)
        and secrets.compare_digest(credentials.password, password)
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Username or Password"
        )

    return {"message": "Authentication Successful!"}