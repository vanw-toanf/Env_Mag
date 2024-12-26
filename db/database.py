import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL


load_dotenv(dotenv_path="../.env")

# create environment variables
username = os.environ.get("DB_USERNAME")
password = os.environ.get("DB_PASSWORD")
host = os.environ.get("DB_HOST")
database = os.environ.get("DB_NAME")

# create database with fastapi
connection_url = URL.create(
    "mysql+mysqlconnector",
    username=username,
    password=password,
    host=host,
    port=3306,
    database=database,
)

engine = create_engine(
    connection_url
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """
    Dung de mo ket noi den SQL Server va thuc hien truy van
    Sau khi truy van tu dong dong ket noi den database
    - **nothing** khong co tham so yeu cau
    `get_db` la ten ham
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


