from sqlalchemy.orm import Session
from models import UserAccount, UserRole
import os
from auth import get_password_hash

SECRET_KEY = os.getenv("SECRET_KEY", "NA")
ALGORITHM = os.getenv("ALGORITHM", "NA")


def check_username(db: Session, username: str):
    r = db.query(UserAccount.username).all()
    if username in [i[0] for i in r]:
        return True
    return False


def check_user_existence(db: Session, email: str):
    r = db.query(UserAccount.email).all()
    if email in [i[0] for i in r]:
        return True
    return False


def get_user(db: Session, username: str):
    user = (
        db.query(UserAccount)
        .filter(UserAccount.username == username)
        .first()
    )
    return user


def get_all_roles(db: Session):
    a = db.query(UserRole.role_id).distinct().all()
    return sorted([i[0] for i in a])


def create_user(db: Session, username: str, password: str, email: str):
    db_user = UserAccount(
        username=username,
        hashed_password=get_password_hash(password),
        email=email,
        password_salt=SECRET_KEY,
        password_hash_algorithm=ALGORITHM,
        role_id=2,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
