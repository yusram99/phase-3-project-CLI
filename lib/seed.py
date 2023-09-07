# seed.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Category, Recipe

engine = create_engine('sqlite:///data/recipe_manager.db')  

Session = sessionmaker(bind=engine)
session = Session()

# Seed data for users
user1 = User(username='user1', password='password1')
user2 = User(username='user2', password='password2')

# Seed data for categories
category1 = Category(name='Desserts')
category2 = Category(name='Main Courses')

# Seed data for recipes
recipe1 = Recipe(
    title='Chocolate Cake',
    ingredients='Chocolate, sugar, flour, eggs',
    instructions='Mix, bake, and enjoy!',
    cooking_time=45,
    servings=8,
    user=user1,
    category=category1
)

recipe2 = Recipe(
    title='Spaghetti Carbonara',
    ingredients='Pasta, eggs, pancetta, cheese',
    instructions='Cook pasta, mix ingredients, and serve.',
    cooking_time=30,
    servings=4,
    user=user2,
    category=category2
)

# Add seed data to the session
session.add_all([user1, user2, category1, category2, recipe1, recipe2])

# Commit the changes to the database
session.commit()

# Close the session
session.close()
