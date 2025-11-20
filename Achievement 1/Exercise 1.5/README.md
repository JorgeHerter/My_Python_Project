Recipe App - Object-Oriented Programming
A Python application that manages recipes using object-oriented programming principles. The app allows you to create recipes, automatically calculate their difficulty levels, and search for recipes by ingredient.
Features

Recipe Management: Create and store recipes with names, ingredients, and cooking times
Automatic Difficulty Calculation: Recipes are automatically categorized as Easy, Medium, Intermediate, or Hard based on cooking time and ingredient count
Ingredient Tracking: Maintains a master list of all unique ingredients across all recipes
Recipe Search: Search for recipes containing specific ingredients

Difficulty Levels
The app automatically calculates recipe difficulty based on the following criteria:
DifficultyCooking TimeNumber of IngredientsEasy< 10 minutes< 4 ingredientsMedium< 10 minutes≥ 4 ingredientsIntermediate≥ 10 minutes< 4 ingredientsHard≥ 10 minutes≥ 4 ingredients
Installation

Ensure you have Python 3.x installed on your system
Download the recipe_oop.py file
No additional dependencies required - uses only Python standard library

Usage
Running the Script
bashpython recipe_oop.py
The script includes example recipes that demonstrate all functionality.
Creating a Recipe
pythonfrom recipe_oop import Recipe

# Initialize a recipe with a name
tea = Recipe("Tea")

# Add ingredients (variable-length arguments)
tea.add_ingredients("Tea Leaves", "Sugar", "Water")

# Set cooking time in minutes
tea.set_cooking_time(5)

# Display the recipe
print(tea)
Using Getter and Setter Methods
python# Get recipe attributes
name = tea.get_name()
cooking_time = tea.get_cooking_time()
ingredients = tea.get_ingredients()
difficulty = tea.get_difficulty()

# Set recipe attributes
tea.set_name("Green Tea")
tea.set_cooking_time(7)
Searching for Recipes by Ingredient
python# Create a list of recipes
recipes_list = [tea, coffee, cake, banana_smoothie]

# Search for recipes containing a specific ingredient
Recipe.recipe_search(recipes_list, "Sugar")
Checking if a Recipe Contains an Ingredient
python# Returns True or False
has_sugar = tea.search_ingredient("Sugar")
Accessing All Ingredients
python# Get all unique ingredients across all recipes
all_ingredients = Recipe.all_ingredients
Example Output
Recipe: Tea
Cooking Time: 5 minutes
Difficulty: Easy
Ingredients:
  - Tea Leaves
  - Sugar
  - Water
Class Structure
Recipe Class
Data Attributes:

name (str): Name of the recipe
ingredients (list): List of ingredients
cooking_time (int): Time in minutes to prepare the recipe
difficulty (str): Auto-calculated difficulty level
all_ingredients (class variable, list): All unique ingredients across all recipes

Methods:

__init__(name): Initialize a new recipe
get_name(): Get recipe name
set_name(name): Set recipe name
get_cooking_time(): Get cooking time
set_cooking_time(time): Set cooking time
add_ingredients(*ingredients): Add ingredients to the recipe
get_ingredients(): Get list of ingredients
calculate_difficulty(): Calculate and set difficulty level
get_difficulty(): Get difficulty (calculates if not set)
search_ingredient(ingredient): Check if ingredient exists in recipe
update_all_ingredients(): Update class-level ingredient list
recipe_search(data, search_term): Search recipes by ingredient (static method)
__str__(): String representation of the recipe

Sample Recipes Included
The script includes four example recipes:

Tea (Easy)

Ingredients: Tea Leaves, Sugar, Water
Cooking Time: 5 minutes


Coffee (Easy)

Ingredients: Coffee Powder, Sugar, Water
Cooking Time: 5 minutes


Cake (Hard)

Ingredients: Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk
Cooking Time: 50 minutes


Banana Smoothie (Medium)

Ingredients: Bananas, Milk, Peanut Butter, Sugar, Ice Cubes
Cooking Time: 5 minutes



Project Structure
recipe-app/
│
├── recipe_oop.py          # Main application file
└── README.md              # This file
Learning Objectives
This project demonstrates:

Object-oriented programming in Python
Class design with data attributes and methods
Getter and setter methods
Class variables vs instance variables
Variable-length arguments (*args)
String representation (__str__)
Automatic property calculation
List traversal and searching

Future Enhancements
Potential improvements for this project:

Save and load recipes from files
User input for creating custom recipes
Recipe rating system
Nutritional information tracking
Recipe categories (breakfast, lunch, dinner, dessert)
Serving size calculations