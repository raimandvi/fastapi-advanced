from fastapi import FastAPI, Depends

app = FastAPI()

# Dependency function
def get_user():
    return {"username": "admin"}


@app.get("/profile")
def read_profile(user: dict = Depends(get_user)):
    return {"message": "User profile", "user": user}
