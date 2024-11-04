from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List

from app import models, schemas, utils, auth
from app.database import SessionLocal, engine

app = FastAPI(
    title="To-Do List API",
    description="An API for managing your To-Do tasks",
    version="1.0.0",
)

# Create tables in the database
models.Base.metadata.create_all(bind=engine)

# OAuth2 scheme for handling the token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# Register Endpoint
@app.post("/register/", response_model=schemas.User, tags=["Users"],
summary="Register a new user", description="Create a new uset for the system.")
def register(user: schemas.UserCreate, db: Session = Depends(utils.get_db)):
    # Check if the username already exists
    existing_user = utils.get_user(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    return utils.create_user(db, user)

@app.post("/login", tags=["Users"],
summary="Login", description="Loggs in user")
async def login(form_data: OAuth2PasswordRequestForm = Depends(),
db: Session = Depends(utils.get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = auth.create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/tasks/", response_model=schemas.Task, tags=["Tasks"],
summary="Create a new task", description="Create a new task for the current user.")
def create_task(
    task: schemas.TaskCreate, 
    db: Session = Depends(utils.get_db),
    current_user: int = Depends(auth.get_current_user)):
    # Create a new task with the owner's ID set to the current user's ID
    return utils.create_task(db, task, current_user.id)


@app.get("/tasks/", response_model=List[schemas.Task],
tags=["Tasks"], summary="Retrieve all tasks",
description="Retrieve a list of all tasks for the current user.")
def read_tasks(
    current_user: schemas.User = Depends(auth.get_current_user), 
    db: Session = Depends(utils.get_db)
):
    return utils.get_tasks(db, current_user.id)

@app.delete("/tasks/{task_id}", tags=["Tasks"],
summary="Delete a task", description="Delete a specific task by its ID.")
def delete_task(task_id: int, current_user: schemas.User = Depends(auth.get_current_user), db: Session = Depends(utils.get_db)):
    utils.delete_task(db, task_id, current_user.id)
    return {"detail": "Task deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
