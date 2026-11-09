import sqlite3

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

print("DELETE API Created Successfully!")