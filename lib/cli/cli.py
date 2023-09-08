import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..models import Recipe  
from ..models import Category  
from ..models import User  

# Defining the SQLAlchemy database connection
engine = create_engine('sqlite:///data/recipe_manager.db')
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    """Recipe Manager CLI"""

# Add recipe
@cli.command()
@click.option('--title', prompt='Recipe Title', help='Title of the recipe')
@click.option('--ingredients', prompt='Ingredients', help='Ingredients of the recipe')
@click.option('--instructions', prompt='Instructions', help='Cooking instructions for the recipe')
@click.option('--cooking-time', type=int, prompt='Cooking Time (minutes)', help='Cooking time in minutes')
@click.option('--servings', type=int, prompt='Servings', help='Number of servings')
@click.option('--username', prompt='Username', help='Username of the recipe creator')
@click.option('--category', prompt='Category', help='Category of the recipe')
def add_recipe(title, ingredients, instructions, cooking_time, servings, username, category):
    """Add a new recipe."""
    session = Session()

    # Find or create the user
    user = session.query(User).filter_by(username=username).first()
    if user is None:
        user = User(username=username, password="your_password_here")
        session.add(user)

    # Find or create the category
    category_obj = session.query(Category).filter_by(name=category).first()
    if category_obj is None:
        category_obj = Category(name=category)
        session.add(category_obj)

    # Create a Recipe object
    recipe = Recipe(title=title, ingredients=ingredients, instructions=instructions, cooking_time=cooking_time, servings=servings, user=user, category=category_obj)

    # Add the recipe to the user's list of recipes
    user.recipes.append(recipe)

    # Add the recipe to the category
    category_obj.recipes.append(recipe)

    # Commit changes to the database
    session.commit()
    session.close()

    # Print a confirmation message
    click.echo(f"Recipe '{title}' added successfully by {username}.")

# view all recipes
@cli.command()
@click.option('--category', help='Filter recipes by category')
def view_recipes(category):
    """View all recipes."""
    session = Session()

    if category:
        # Filter and display recipes by category
        recipes = session.query(Recipe).join(Recipe.category).filter(Category.name == category).all()
    else:
        # Retrieve and display all recipes
        recipes = session.query(Recipe).all()

    # Print recipes
    for recipe in recipes:
        click.echo(f"Title: {recipe.title}")
        click.echo(f"Ingredients: {recipe.ingredients}")
        click.echo(f"Instructions: {recipe.instructions}")
        click.echo(f"Cooking Time: {recipe.cooking_time} minutes")
        click.echo(f"Servings: {recipe.servings}")
        click.echo(f"Created by: {recipe.user.username}")
        click.echo('-' * 20)

    session.close()

# update an existing recipe
@cli.command()
@click.option('--title', prompt='Recipe Title', help='Title of the recipe to update')
@click.option('--ingredients', prompt='Ingredients', help='Updated ingredients of the recipe')
@click.option('--instructions', prompt='Instructions', help='Updated cooking instructions')
@click.option('--cooking-time', type=int, prompt='Cooking Time (minutes)', help='Updated cooking time')
@click.option('--servings', type=int, prompt='Servings', help='Updated servings')
@click.option('--username', prompt='Username', help='Username of the recipe creator')
def update_recipe(title, ingredients, instructions, cooking_time, servings, username):
    """Update an existing recipe."""
    session = Session()

    # Find the recipe by title and username
    recipe = session.query(Recipe).join(Recipe.user).filter(Recipe.title == title, User.username == username).first()
    if recipe is None:
        click.echo(f"Recipe '{title}' not found for user '{username}'.")
    else:
        # Update recipe details
        recipe.title = title
        recipe.ingredients = ingredients
        recipe.instructions = instructions
        recipe.cooking_time = cooking_time
        recipe.servings = servings
        session.commit()
        click.echo(f"Recipe '{title}' updated successfully.")

    session.close()

# delete a recipe
@cli.command()
@click.option('--title', prompt='Recipe Title', help='Title of the recipe to delete')
@click.option('--username', prompt='Username', help='Username of the recipe creator')
def delete_recipe(title, username):
    """Delete a recipe."""
    session = Session()

    # Find the recipe by title and username
    recipe = session.query(Recipe).join(Recipe.user).filter(Recipe.title == title, User.username == username).first()
    if recipe is None:
        click.echo(f"Recipe '{title}' not found for user '{username}'.")
    else:
        # Delete the recipe
        session.delete(recipe)
        session.commit()
        click.echo(f"Recipe '{title}' deleted successfully.")

    session.close()

# sort recipes by title 
@cli.command()
def sort_recipes():
    """Sort recipes by title in ascending order."""
    session = Session()

    # Retrieve and display all recipes sorted by title
    recipes = session.query(Recipe).order_by(Recipe.title.asc()).all()

    # Print sorted recipes
    for recipe in recipes:
        click.echo(f"Title: {recipe.title}")
        click.echo(f"Ingredients: {recipe.ingredients}")
        click.echo(f"Instructions: {recipe.instructions}")
        click.echo('-' * 20)

    session.close()

# search recipes
@cli.command()
@click.option('--category', help='Filter recipes by category')
@click.option('--keyword', help='Keyword to search for in recipe title or ingredients')
def search_recipes(category, keyword):
    """Search and filter recipes based on category and keyword."""
    session = Session()
    query = session.query(Recipe)

    if category:
        # Filter recipes by category
        query = query.join(Recipe.category).filter(Category.name == category)

    if keyword:
        # Search for recipes containing the keyword in title or ingredients
        query = query.filter(
            (Recipe.title.like(f"%{keyword}%")) | (Recipe.ingredients.like(f"%{keyword}%"))
        )

    # Retrieve and display matching recipes
    recipes = query.all()

    if not recipes:
        click.echo("No matching recipes found.")
    else:
        # Print matching recipes
        for recipe in recipes:
            click.echo(f"Title: {recipe.title}")
            click.echo(f"Ingredients: {recipe.ingredients}")
            click.echo(f"Instructions: {recipe.instructions}")
            click.echo(f"Cooking Time: {recipe.cooking_time} minutes")
            click.echo(f"Servings: {recipe.servings}")
            click.echo(f"Created by: {recipe.user.username}")
            click.echo('-' * 20)

    session.close()

if __name__ == '__main__':
    cli()
