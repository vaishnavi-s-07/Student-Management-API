from pydantic import BaseModel
import sqlite3

class Student(BaseModel):
    name: str
    email: str
    course: str

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
    return {"message": "Student Created Successfully!", "student_id": student_id}

print("POST API Created Successfully!")