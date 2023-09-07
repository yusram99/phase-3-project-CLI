# test_recipe_manager.py

from cli.cli import cli
import click
import pytest

@pytest.fixture
def runner():
    return click.testing.CliRunner()

def test_add_recipe(runner):
    result = runner.invoke(cli, ['add_recipe', '--title', 'Test Recipe', '--ingredients', 'Ingredient 1', '--instructions', 'Step 1', '--cooking-time', '30', '--servings', '4', '--username', 'user'])
    assert 'Recipe' in result.output
    assert 'added successfully' in result.output

# Add more test cases for other commands...

if __name__ == '__main__':
    pytest.main()
