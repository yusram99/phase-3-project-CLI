# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    recipes = relationship('Recipe', back_populates='user')

# Define Category model
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    recipes = relationship('Recipe', back_populates='category')

# Define Recipe model
class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    ingredients = Column(String(500), nullable=False)
    instructions = Column(String(1000), nullable=False)
    cooking_time = Column(Integer)
    servings = Column(Integer)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='recipes')

    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='recipes')

# Create the database and tables
engine = create_engine('sqlite:///recipe_manager.db')
Base.metadata.create_all(engine)


