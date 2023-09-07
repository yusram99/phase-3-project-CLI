# user.py

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.recipes = []  # List to store recipes created by this user

    def authenticate_user(self, entered_password):
        return self.password == entered_password

    def view_user_recipes(self):
        if not self.recipes:
            return "You haven't created any recipes yet."
        
        recipes_list = "\n".join([recipe.title for recipe in self.recipes])
        return f"Recipes created by {self.username}:\n{recipes_list}"
