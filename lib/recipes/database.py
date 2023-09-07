from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./data/recipe_manager.db"

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for your models
Base = declarative_base()
