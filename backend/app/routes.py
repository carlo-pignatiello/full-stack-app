from fastapi import APIRouter, Depends, HTTPException, status
import models
from database import SessionLocal, engine
from repos import get_user
from sqlalchemy.orm import Session
from schemas import TokenRequest, TokenSchema
from auth import verify_password, create_access_token

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.post("/login", response_model=TokenSchema)
def login(request: TokenRequest, db: Session = Depends(get_db)):
    user = get_user(db, request.username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email"
        )
    hashed_pass = user.password
    if not verify_password(request.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password"
        )

    access = create_access_token(user.id)
    # refresh = create_refresh_token(user.id)

    return TokenSchema(
        access_token=access
    )
