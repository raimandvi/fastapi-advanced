from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, SessionLocal
from models import Base, Student
from schemas import StudentCreate, StudentResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):

    new_student = Student(
        name=student.name,
        email=student.email
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
