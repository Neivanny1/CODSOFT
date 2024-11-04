from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_time: Optional[datetime] = None  # Optional due time

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None  # Make description optional
    completed: bool
    date_created: datetime
    due_time: Optional[datetime] = None
    owner_id: int  # Include owner_id to identify the user who created the task

    class Config:
        orm_mode = True
