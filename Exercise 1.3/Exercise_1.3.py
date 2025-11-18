recipes_list = []
ingredients_list = []

def take_recipe():
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
    
    # Create recipe dictionary
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    
    return recipe

# Main section
n = int(input("How many recipes would you like to enter? "))

# Loop to collect n recipes
for i in range(n):
    print(f"\nRecipe {i + 1}:")
    recipe = take_recipe()
    
    # Loop through ingredients in the recipe
    for ingredient in recipe['ingredients']:
        # Check if ingredient is not already in ingredients_list
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    
    # Add recipe to recipes_list
    recipes_list.append(recipe)

# Loop through recipes_list to determine difficulty
for recipe in recipes_list:
    cooking_time = recipe['cooking_time']
    num_ingredients = len(recipe['ingredients'])
    
    # Determine difficulty based on cooking time and number of ingredients
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    elif cooking_time >= 10 and num_ingredients >= 4:
        difficulty = "Hard"
    
    # Display recipe with difficulty
    print(f"\nRecipe: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Difficulty: {difficulty}")

# Display all ingredients in alphabetical order
print("\n" + "="*50)
print("Ingredients Available Across All Recipes:")
print("="*50)
ingredients_list.sort()
for ingredient in ingredients_list:
    print(ingredient)