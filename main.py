from fastapi import FastAPI, status
from pydantic import BaseModel
from fastapi.responses import PlainTextResponse
from typing import List
app = FastAPI()

students_db = []

Class Student(BaseModel):
Reference: str
FirstName: str
LastName: str
Age: int

@app.get("/hello", response_class=PlainTextResponse)
def say_hello():
    return "Hello world";

@app.get("/welcome")
def welcome(name: str):
    return {"message": f"Welcome {name}"}

@app.post("/students", status_code=status.HTTP_201_CREATED)
def add_students(students: List[Student]):
    for student in students:
        students_db.append(student)
        return students_db

@app.get("/student")
def get_students():
    return students_db

@app.put("/students")
def update_or_add_student(student: Student):
    for index, existing in enumerate(students_db):
    if existing.Reference == student.Reference:
        if existing != student:
            students_db[index] = student
        return students_db
    students_db.append(student)
    return students_db