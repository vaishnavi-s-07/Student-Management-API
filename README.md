Student Management API

Project Overview

A Student Management REST API developed using Python, FastAPI, and SQLite.

Technologies Used

- Python
- FastAPI
- SQLite
- Pydantic
- Google Colab

Features

1. Create Student – POST
2. View Students – GET
3. Update Student – PUT
4. Delete Student – DELETE
5. Basic Authentication
6. API Testing

API Endpoints

Method| Endpoint| Description
GET| /| Home
GET| /students| View all students
POST| /students| Add student
PUT| /students/{student_id}| Update student
DELETE| /students/{student_id}| Delete student
GET| /secure| Authentication

Database

SQLite database is used to store student details.

Authentication

Basic Authentication is implemented to protect the secure endpoint.

Testing

API endpoints were tested using FastAPI TestClient.

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run the application:
   uvicorn main:app --reload

3. Open API documentation:
   /docs

## Main Application

The main.py file integrates all API endpoints, database operations, and authentication.

Conclusion

The Student Management API successfully demonstrates CRUD operations, database connectivity, authentication, and REST API testing.
