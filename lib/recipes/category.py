# category.py

class Category:
    def __init__(self, name):
        self.name = name
        self.recipes = []  # List to store recipes in this category

    def __str__(self):
        return self.name

    def view_recipes_in_category(self):
        if not self.recipes:
            return "No recipes in this category."
        
        recipes_list = "\n".join([recipe.title for recipe in self.recipes])
        return f"Recipes in {self.name} category:\n{recipes_list}"

    def add_recipe_to_category(self, recipe):
        self.recipes.append(recipe)
