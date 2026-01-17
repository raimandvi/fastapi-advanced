from fastapi import APIRouter
router = APIRouter()

@router.get("/students")
def get_students():
    return {"message": "List of students"}