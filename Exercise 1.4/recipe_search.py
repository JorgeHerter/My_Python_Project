# Step 1: Import pickle module
import pickle

# Step 2: Define display_recipe() function
def display_recipe(recipe):
    print("="*50)
    print(f"Recipe: {recipe['name']}")
    print("="*50)
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print(f"Difficulty: {recipe['difficulty']}")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"  - {ingredient}")
    print("="*50)

# Step 3: Define search_ingredient() function
def search_ingredient(data):
    print("Available ingredients:")
    print("="*50)
    all_ingredients = data['all_ingredients']
    for index, ingredient in enumerate(all_ingredients):
        print(f"{index}. {ingredient}")
    print("="*50)
    try:
        ingredient_index = int(input("Enter the number of the ingredient you want to search for: "))
        ingredient_searched = all_ingredients[ingredient_index]
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except IndexError:
        print("The number you entered is out of range. Please try again.")
    except:
        print("An error occurred. Please try again.")
    else:
        print(f"Recipes containing '{ingredient_searched}':")
        print("="*50)
        found = False
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
                display_recipe(recipe)
                found = True
        if not found:
            print(f"No recipes found with {ingredient_searched}.")

# Main code
filename = input("Enter the filename containing your recipe data: ")

try:
    file = open(filename, 'rb')
    data = pickle.load(file)
except FileNotFoundError:
    print("File not found. Please make sure the file exists and try again.")
except:
    print("An error occurred while loading the file.")
else:
    file.close()
    search_ingredient(data)