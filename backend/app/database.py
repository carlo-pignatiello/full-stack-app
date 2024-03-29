from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

user = os.getenv("POSTGRES_USER", "NA")
password = os.getenv("POSTGRES_PASSWORD", "NA")
database = os.getenv("POSTGRES_DATABASE", "NA")
host = os.getenv("POSTGRES_HOST", "NA")
port = os.getenv("POSTGRES_PORT", "NA")

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{database}"
print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

