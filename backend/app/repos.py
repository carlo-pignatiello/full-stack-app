import models
from sqlalchemy.orm import Session


def get_user(db: Session, user_name: str):
    user = (
        db.query(models.UserAccount)
        .filter(models.UserAccount.user_name == user_name)
        .first()
    )
    return user


def create_user(db: Session, db_user: models.UserAccount):
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
