from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import time
from .config import settings

# Database URL from settings
SQLALCHEMY_DATABASE_URL = settings.DATABASEURL

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for the ORM models
Base = declarative_base()

# Dependency to get a new database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
