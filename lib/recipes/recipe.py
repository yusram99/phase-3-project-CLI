from sqlalchemy import Column, Integer, String, ForeignKey, Float  # Import Float data type
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

    # Add these two fields for rating
    total_ratings = Column(Integer, default=0)
    average_rating = Column(Float, default=0.0)

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

    def calculate_average_rating(self, new_rating):
        # Calculate the new average rating
        total_ratings = self.total_ratings + 1
        current_average = self.average_rating
        new_average = (current_average * (total_ratings - 1) + new_rating) / total_ratings
        self.total_ratings = total_ratings
        self.average_rating = new_average
