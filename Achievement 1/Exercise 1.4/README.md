# Exercise 1.4 - Recipe Storage and Search with Pickle

## Overview
This exercise introduces binary file handling using Python's `pickle` module. The project consists of two scripts that work together: one for storing recipes and another for searching through them. This demonstrates persistent data storage, allowing recipes to be saved and retrieved across multiple sessions.

## Scripts

### 1. recipe_input.py
A script that collects recipes from users and stores them in a binary file using the pickle module.

**Features:**
- Takes recipe input (name, cooking time, ingredients) from users
- Automatically calculates recipe difficulty based on cooking time and ingredient count
- Loads existing recipe data from a binary file (if it exists)
- Appends new recipes to the existing collection
- Tracks all unique ingredients across all recipes
- Saves all data back to the binary file

### 2. recipe_search.py
A script that searches for recipes containing a specific ingredient.

**Features:**
- Loads recipe data from a binary file
- Displays all available ingredients with numbered indices
- Allows users to select an ingredient by number
- Searches and displays all recipes containing the selected ingredient
- Handles errors gracefully (file not found, invalid input, etc.)

## Difficulty Calculation Logic

Recipes are automatically assigned a difficulty level based on two criteria:

| Cooking Time | Ingredients | Difficulty |
|--------------|-------------|------------|
| < 10 minutes | < 4 items   | Easy       |
| < 10 minutes | ≥ 4 items   | Medium     |
| ≥ 10 minutes | < 4 items   | Intermediate |
| ≥ 10 minutes | ≥ 4 items   | Hard       |

## How to Run

### Adding Recipes (recipe_input.py)

1. Activate your virtual environment
2. Run the input script:
   ```bash
   python recipe_input.py
   ```
3. Enter a filename to store your recipes (e.g., `recipes.bin`)
4. Follow the prompts to enter recipes:
   - Recipe name
   - Cooking time (in minutes)
   - Ingredients (one at a time, type 'done' when finished)
5. Repeat for as many recipes as you'd like to add

**Example:**
```
Enter the filename where you'd like to store your recipes: recipes.bin
File doesn't exist - creating a new one.
How many recipes would you like to enter? 2

Recipe 1:
Enter the recipe name: Tea
Enter the cooking time (in minutes): 5
Enter ingredients (type 'done' when finished):
Enter an ingredient: Tea Leaves
Enter an ingredient: Water
Enter an ingredient: Sugar
Enter an ingredient: done

Recipe 2:
Enter the recipe name: Spaghetti
Enter the cooking time (in minutes): 20
Enter ingredients (type 'done' when finished):
Enter an ingredient: Pasta
Enter an ingredient: Tomato Sauce
Enter an ingredient: Garlic
Enter an ingredient: Olive Oil
Enter an ingredient: done

Recipes successfully saved to recipes.bin!
```

### Searching Recipes (recipe_search.py)

1. Run the search script:
   ```bash
   python recipe_search.py
   ```
2. Enter the filename containing your recipe data
3. Select an ingredient number from the displayed list
4. View all recipes containing that ingredient

**Example:**
```
Enter the filename containing your recipe data: recipes.bin

Available ingredients:
==================================================
0. Tea Leaves
1. Water
2. Sugar
3. Pasta
4. Tomato Sauce
5. Garlic
6. Olive Oil
==================================================

Enter the number of the ingredient you want to search for: 1

Recipes containing 'Water':
==================================================
Recipe: Tea
==================================================
Cooking Time: 5 minutes
Difficulty: Easy
Ingredients:
  - Tea Leaves
  - Water
  - Sugar
==================================================
```

## Data Structure

The binary file stores a dictionary with two keys:

```python
{
    'recipes_list': [
        {
            'name': 'Tea',
            'cooking_time': 5,
            'ingredients': ['Tea Leaves', 'Water', 'Sugar'],
            'difficulty': 'Easy'
        },
        # ... more recipes
    ],
    'all_ingredients': ['Tea Leaves', 'Water', 'Sugar', 'Pasta', ...]
}
```

## Key Concepts Practiced

- **Binary file handling** with Python's `pickle` module
- **Persistent data storage** - data survives between program runs
- **Exception handling** with try-except-else-finally blocks
- **Dictionary and list manipulation**
- **Function definition and organization**
- **User input validation**
- **Data serialization and deserialization**

## Error Handling

Both scripts include robust error handling:

- **FileNotFoundError**: Creates a new data file if none exists
- **ValueError**: Handles invalid numeric input
- **IndexError**: Handles out-of-range ingredient selections
- **General exceptions**: Catches unexpected errors gracefully

## Files in This Exercise

- `recipe_input.py` - Script for adding recipes
- `recipe_search.py` - Script for searching recipes
- `recipes.bin` - Binary file containing recipe data (generated after first run)
- Screenshots of execution steps
- Learning journal entries

## Notes

- The binary file (`.bin`) uses pickle serialization, which is Python-specific
- You can run `recipe_input.py` multiple times to keep adding recipes to the same file
- Ingredient tracking automatically avoids duplicates
- All ingredients are stored exactly as entered (case-sensitive)
- The difficulty is calculated and stored when recipes are created