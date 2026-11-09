import sqlite3
from pydantic import BaseModel

class UpdateStudent(BaseModel):
    name: str
    email: str
    course: str

@app.put("/students/{student_id}")
def update_student(student_id: int, student: UpdateStudent):

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

print("UPDATE API Created Successfully!")