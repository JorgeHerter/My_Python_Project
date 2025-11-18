# Exercise 1.3 - Recipe Management System

## Overview
This exercise involves creating a Python script that collects recipes from users, tracks ingredients across all recipes, calculates difficulty levels, and displays the information in an organized format.

**Estimated Time:** 1-3 hours

## Objectives
- Accept multiple recipes from user input
- Store recipes in a list with their details (name, cooking time, ingredients)
- Track all unique ingredients across recipes
- Calculate and display difficulty levels for each recipe
- Display all ingredients in alphabetical order

## Features
- **Recipe Input:** Collect recipe name, cooking time, and ingredients from the user
- **Ingredient Tracking:** Maintain a list of all unique ingredients across recipes
- **Difficulty Calculation:** Automatically determine recipe difficulty based on cooking time and ingredient count
- **Formatted Output:** Display recipes with their details and difficulty levels

## Difficulty Levels
The difficulty of each recipe is calculated based on two factors:

| Cooking Time | Ingredients | Difficulty |
|--------------|-------------|------------|
| < 10 minutes | < 4 items   | Easy       |
| < 10 minutes | ≥ 4 items   | Medium     |
| ≥ 10 minutes | < 4 items   | Intermediate |
| ≥ 10 minutes | ≥ 4 items   | Hard       |

## How to Run
1. Ensure Python 3.x is installed on your system
2. Navigate to the Exercise 1.3 directory
3. Run the script:
   ```bash
   python Exercise_1.3.py
   ```
4. Follow the prompts to enter your recipes

## Script Structure
- **recipes_list:** Stores all recipe dictionaries
- **ingredients_list:** Stores all unique ingredients across recipes
- **take_recipe():** Function to collect recipe input from the user
- **Main section:** 
  - Collects number of recipes to enter
  - Loops to gather recipe data
  - Calculates and displays difficulty for each recipe
  - Shows all ingredients in alphabetical order

## Example Usage
```
How many recipes would you like to enter? 2

Recipe 1:
Enter the recipe name: Toast
Enter the cooking time (in minutes): 5
Enter ingredients (type 'done' when finished):
Enter an ingredient: bread
Enter an ingredient: butter
Enter an ingredient: done

Recipe 2:
Enter the recipe name: Lasagna
Enter the cooking time (in minutes): 60
Enter ingredients (type 'done' when finished):
Enter an ingredient: pasta
Enter an ingredient: meat
Enter an ingredient: cheese
Enter an ingredient: tomato sauce
Enter an ingredient: done

Recipe: Toast
Cooking Time: 5 minutes
Ingredients: bread, butter
Difficulty: Easy

Recipe: Lasagna
Cooking Time: 60 minutes
Ingredients: pasta, meat, cheese, tomato sauce
Difficulty: Hard

==================================================
Ingredients Available Across All Recipes:
==================================================
bread
butter
cheese
meat
pasta
tomato sauce
```

## Deliverables
- `Exercise_1.3.py` - Main Python script
- Screenshots of each step in execution
- Updated learning journal

## Key Concepts Practiced
- Lists and dictionaries
- User input handling
- For loops and nested loops
- Conditional statements
- String formatting
- List sorting
- Function definition and usage

## Notes
- Enter ingredients one at a time, typing 'done' when finished
- Cooking time should be entered in minutes as an integer
- The script tracks unique ingredients automatically (no duplicates)
- Ingredients are displayed in alphabetical order at the end