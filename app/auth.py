from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User
from app.schemas import UserCreate, UserLogin
import hashlib

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()
    

# @router.post("/signup")
# def signup(user: UserCreate, db: Session = Depends(get_db)):
#     existing_user = db.query(User).filter(User.username == user.username).first()
#     if existing_user:
#         raise HTTPException(status_code=400, detail="Username already exists")

#     # new_user = User(username=user.username, password=user.password)
#     new_user = User(username=user.username, password=hash_password(user.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return {"message": "User created successfully"}
@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")

    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully"}


# @router.post("/login")
# def login(user: UserLogin, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(
#     User.username == user.username,
#     User.password == hash_password(user.password)
#     ).first()
#     if not db_user:
#         raise HTTPException(status_code=400, detail="Invalid credentials")
#     return {"message": "Login successful", "username": user.username}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(
        (User.username == user.identifier) | (User.email == user.identifier),
        User.password == hash_password(user.password)
    ).first()
    
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    return {"message": "Login successful", "username": db_user.username}
