from sqlalchemy.orm import Session
from . import models, schemas, database
from passlib.hash import bcrypt

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = bcrypt.hash(user.password)
    db_user = models.User(username=user.username, password_hash=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_task(db: Session, task: schemas.TaskCreate, owner_id: int):
    # Create a new Task instance with the provided owner_id
    db_task = models.Task(owner_id=current_user.id, **task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks(db: Session, user_id: int):
    return db.query(models.Task).filter(models.Task.owner_id == user_id).all()
