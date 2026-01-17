from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

# Request model
class StudentCreate(BaseModel):
    name: str
    age: int
    email: str
    password: str

# Response model
class StudentResponse(BaseModel):
    name: str
    age: int
    email: str


@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(student: StudentCreate):
    return student
