from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


SQLALCHEMY_DATABASE_URL = settings.database_url

# create a sqlalchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create a configured "Base" class
Base = declarative_base()

# Function will be used as a dependency in the models.py file
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

