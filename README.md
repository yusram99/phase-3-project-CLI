## Recipe Manager CLI
# Description
The Recipe Manager CLI is a command-line tool that allows users to manage and organize their recipes. With this CLI, you can add, view, update, and delete recipes. It provides a convenient way to keep track of your favorite recipes and cooking instructions.

# Features
- Add Recipe: Add a new recipe with a title, ingredients, cooking instructions, cooking time, servings, and your username.

- View Recipes: View all recipes or filter them by category.

- Update Recipe: Update the details of an existing recipe, including title, ingredients, instructions, cooking time, and servings.

- Delete Recipe: Delete a recipe by specifying its title and your username.

- Sort Recipes: Sort all recipes by title in ascending order.

# Installation
1. Clone this repository to your local machine.
git clone https://github.com/your-yusram/recipe-manager-cli.git

2. Navigate to the project directory.
cd recipe-manager-cli

3. Install the required dependencies.
pip install -r requirements.txt


# Usage
1. Adding a Recipe
- To add a new recipe, run the following command:
python -m lib.cli.cli add-recipe

2. Viewing Recipes
- To view all recipes, run the following command:
python -m lib.cli.cli view-recipes

3. To filter recipes by category, use the --category option.
- python -m lib.cli.cli view-recipes --category <category_name>
python -m lib.cli.cli add-recipe --category Breakfast
python -m lib.cli.cli add-recipe --category Lunch
python -m lib.cli.cli add-recipe --category Dinner


4. Updating a Recipe
- To update an existing recipe, run the following command:
python -m lib.cli.cli update-recipe

5. Deleting a Recipe
To delete a recipe, run the following command:
python -m lib.cli.cli delete-recipe
Follow the prompts to specify the recipe title and your username.

6.  Sorting Recipes
To sort recipes by title in ascending order, run the following command:
python -m lib.cli.cli sort-recipes

7.  view all the commands availabe 
python -m lib.cli.cli --help

# Configuration
The project uses an SQLite database for data storage. You can configure the database connection in the lib.cli.cli script by modifying the create_engine line.

# Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your fork.
5. Create a pull request to merge your changes into the main repository.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

