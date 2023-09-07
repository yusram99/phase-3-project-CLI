# recipe.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    ingredients = Column(String)
    instructions = Column(String)
    cooking_time = Column(Integer)
    servings = Column(Integer)

    # Define a foreign key relationship to the User table
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="recipes")

    def __init__(self, title=None, ingredients=None, instructions=None, cooking_time=None, servings=None, user=None):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.cooking_time = cooking_time
        self.servings = servings
        self.user = user

    def update_recipe(self, title, ingredients, instructions, cooking_time, servings):
        # Update the recipe attributes
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.cooking_time = cooking_time
        self.servings = servings