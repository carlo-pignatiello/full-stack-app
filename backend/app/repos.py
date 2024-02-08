import models
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()


def get_user(user_name: str):
    user = (
        db.query(models.UserAccount)
        .filter(models.UserAccount.user_name == user_name)
        .first()
    )
    return user


def create_user():
    db_user = models.UserAccount(
        user_name="silvia",
        email='silvia@silvia',
        hashed_password = "afbwuybwibauybfibfwyab",
        password_salt="afawf",
        password_hash_algorithm="SHA-256",
        role_id=1
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


if __name__ == "__main__":
    user = get_user("carlo")
    res = create_user()
    print(res)
