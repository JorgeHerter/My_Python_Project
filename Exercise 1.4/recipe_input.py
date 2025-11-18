# Step 1: Import pickle module
import pickle

# Step 2: Define take_recipe() function
def take_recipe():
    """
    Takes recipe input from the user and returns a recipe dictionary.
    """
    # Get recipe name from user
    name = input("Enter the recipe name: ")
    
    # Get cooking time from user (convert to int)
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    
    # Get ingredients from user
    ingredients = []
    print("Enter ingredients (type 'done' when finished):")
    while True:
        ingredient = input("Enter an ingredient: ")
        if ingredient.lower() == 'done':
            break
        ingredients.append(ingredient)
    
    # Calculate difficulty
    difficulty = calc_difficulty(cooking_time, len(ingredients))
    
    # Create recipe dictionary
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
        'difficulty': difficulty
    }
    
    return recipe
def calc_difficulty(cooking_time, num_ingredients):
    """
    Calculates the difficulty level of a recipe based on cooking time and number of ingredients.
    
    Parameters:
    - cooking_time (int): Cooking time in minutes
    - num_ingredients (int): Number of ingredients in the recipe
    
    Returns:
    - str: Difficulty level ('Easy', 'Medium', 'Intermediate', or 'Hard')
    """
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    else:  # cooking_time >= 10 and num_ingredients >= 4
        difficulty = "Hard"
    
    return difficulty
# Main code
filename = input("Enter the filename where you'd like to store your recipes: ")

try:
    # Try to open the file in read binary mode
    file = open(filename, 'rb')
    data = pickle.load(file)

except FileNotFoundError:
    # If file doesn't exist, create new data dictionary
    print("File doesn't exist - creating a new one.")
    data = {
        'recipes_list': [],
        'all_ingredients': []
    }

except:
    # Handle any other exceptions
    print("An error occurred. Creating a new data file.")
    data = {
        'recipes_list': [],
        'all_ingredients': []
    }

else:
    # Close the file if it was successfully opened
    file.close()

finally:
    # Extract the lists from the data dictionary
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']

    # Ask user how many recipes to enter
n = int(input("How many recipes would you like to enter? "))

# Loop to collect n recipes
for i in range(n):
    print(f"\nRecipe {i + 1}:")
    recipe = take_recipe()
    recipes_list.append(recipe)
    
    # Inner loop to add new ingredients to all_ingredients
    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

  # Gather updated lists into data dictionary
data = {
    'recipes_list': recipes_list,
    'all_ingredients': all_ingredients
} 

# Open file in write binary mode and save data
with open(filename, 'wb') as file:
    pickle.dump(data, file)

print(f"\nRecipes successfully saved to {filename}!")