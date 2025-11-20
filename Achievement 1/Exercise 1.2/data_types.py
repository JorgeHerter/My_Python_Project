# This file contains the data structure for Exercise 1.2,
# demonstrating the use of nested Python data structures.

# --- Recipe Definitions (Dictionary Structures) ---

recipe_1 = {
    "name": "Tea",
    "cooking_time": 5,
    "ingredients": ["Tea leaves", "Sugar", "Water"]
}

recipe_2 = {
    "name": "Scrambled Eggs",
    "cooking_time": 10,
    "ingredients": ["Eggs", "Milk", "Butter", "Salt", "Pepper"]
}

recipe_3 = {
    "name": "Simple Salad",
    "cooking_time": 15,
    "ingredients": ["Lettuce", "Tomatoes", "Cucumber", "Olive oil", "Vinegar"]
}

recipe_4 = {
    "name": "Oatmeal",
    "cooking_time": 7,
    "ingredients": ["Oats", "Water", "Milk", "Honey"]
}

recipe_5 = {
    "name": "Grilled Cheese Sandwich",
    "cooking_time": 8,
    "ingredients": ["Bread", "Cheese", "Butter"]
}

all_recipes = []
all_recipes.append(recipe_1)
all_recipes.append(recipe_2)
all_recipes.append(recipe_3)
all_recipes.append(recipe_4)
all_recipes.append(recipe_5)

print(f"Recipe Name: {recipe_1['name']}")
print(f"Preparation Time: {recipe_1['cooking_time']} minutes")
print(f"Key Ingredient: {recipe_1['ingredients'][0]}")