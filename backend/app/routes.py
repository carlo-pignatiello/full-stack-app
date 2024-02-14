from fastapi import APIRouter, Depends, HTTPException, status
from models import Base
from database import SessionLocal, engine
from repos import create_user, check_user_existence, check_username, get_user
from sqlalchemy.orm import Session
from schemas import RegistrationSchema, TokenSchema, TokenRequest
from auth import verify_password, create_access_token, refresh_access_token


Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


user_router = APIRouter()


@user_router.post("/signup")
def signup(request: RegistrationSchema, db: Session = Depends(get_db)):
    user_exists = check_user_existence(db=db, email=request.email)
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
        ) 
    user_name = check_username(db=db, username=request.username)
    if user_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists"
        )
    create_user(
        db, username=request.username, password=request.password, email=request.email
    )
    return {"status": "user_created"}


@user_router.post("/signin", response_model=TokenSchema)
def login(request: TokenRequest, db: Session = Depends(get_db)):
    user = get_user(db, request.username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email"
        )
    hashed_pass = user.hashed_password
    if not verify_password(request.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password"
        )
    access = create_access_token(user.id)
    refresh = refresh_access_token(user.id)
    return TokenSchema(access_token=access, refresh_token=refresh)
