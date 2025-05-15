from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base  # ✅ new import


# Create the SQLite engine
DATABASE_URL = "sqlite:///./summarizers.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a base class for models
Base = declarative_base()

# Create a session factory
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Initialize DB (to be called in main.py)
def init_db():
    from app import models  # Import models so they get registered
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()