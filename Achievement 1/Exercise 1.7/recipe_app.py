# Import necessary packages and methods
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_ # Import or_ for potential future multi-condition searches

# Database credentials
USERNAME = 'cf-python'
PASSWORD = 'password'
HOSTNAME = 'localhost'
DATABASE = 'task_database'

# Create engine object that connects to the database
engine = create_engine(f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOSTNAME}/{DATABASE}')

# Generate Session class and bind it to the engine
Session = sessionmaker(bind=engine)

# Initialize session object
session = Session()

# Create declarative base for model definitions
Base = declarative_base()

# Model Definition (to be completed in Part 2)
class Recipe(Base):
    """Recipe model for storing recipe information in the database."""
    __tablename__ = 'final_recipes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))
    
    def __repr__(self):
        return f"<Recipe(id={self.id}, name='{self.name}', difficulty='{self.difficulty}')>"
    
    def __str__(self):
        """Return a formatted string representation of the recipe."""
        output = f"\n{'='*50}\n"
        output += f"Recipe ID: {self.id}\n"
        output += f"Name: {self.name}\n"
        output += f"Ingredients: {self.ingredients}\n"
        output += f"Cooking Time: {self.cooking_time} minutes\n"
        output += f"Difficulty: {self.difficulty}\n"
        output += f"{'='*50}"
        return output
    
    def calculate_difficulty(self):
        """Calculate and set the difficulty based on cooking time and ingredients."""
        ingredients_list = self.ingredients.split(', ')
        num_ingredients = len(ingredients_list)
        
        if self.cooking_time < 10:
            if num_ingredients < 4:
                self.difficulty = "Easy"
            else:
                self.difficulty = "Medium"
        else:
            if num_ingredients < 4:
                self.difficulty = "Intermediate"
            else:
                self.difficulty = "Hard"
    
    def return_ingredients_as_list(self):
        """Return ingredients as a list."""
        if not self.ingredients:
            return []
        return self.ingredients.split(', ')

# Create all tables in the database
Base.metadata.create_all(engine)

# --------------------------------------------------------------------------
# --- Main Menu Function (Updated/Implemented) ---
# --------------------------------------------------------------------------

def main_menu():
    """Display main menu and handle user choices."""
    print("\n" + "="*50)
    print("RECIPE APP - Main Menu")
    print("="*50)
    
    choice = ""
    while choice != "quit":
        print("\nWhat would you like to do? Pick a choice!")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for recipes by ingredient")
        print("4. Update an existing recipe")
        print("5. Delete a recipe")
        print("Type 'quit' to exit the program")
        
        choice = input("\nYour choice: ").strip().lower()
        
        if choice == "1":
            create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            search_by_ingredient()
        elif choice == "4":
            edit_recipe()
        elif choice == "5":
            delete_recipe()
        elif choice == "quit":
            print("\n" + "="*50)
            print("Closing the Recipe App. Goodbye!")
            print("="*50)
        else:
            print("\nInvalid choice. Please try again.")
            
    # Close the session and dispose the engine when the user quits
    session.close()
    engine.dispose()

# --------------------------------------------------------------------------
# --- Recipe Management Functions (No Changes Made Here) ---
# --------------------------------------------------------------------------

def create_recipe():
    """Create a new recipe and add it to the database."""
    print("\n" + "="*50)
    print("CREATE NEW RECIPE")
    print("="*50)
    
    # Get recipe name with validation
    while True:
        name = input("\nEnter recipe name: ").strip()
        if len(name) == 0:
            print("Recipe name cannot be empty. Try again.")
        elif len(name) > 50:
            print("Recipe name too long! Maximum 50 characters.")
        else:
            break
            
    # Get cooking time with validation
    while True:
        cooking_time_input = input("Enter cooking time (in minutes): ").strip()
        if not cooking_time_input.isnumeric():
            print("Invalid input. Cooking time must be a number.")
        else:
            cooking_time = int(cooking_time_input)
            if cooking_time > 0:
                break
            else:
                print("Cooking time must be positive. Try again.")
                
    # Collect ingredients using a for loop
    ingredients = []
    while True:
        num_ingredients_input = input("\nHow many ingredients would you like to enter? ").strip()
        if not num_ingredients_input.isnumeric():
            print("Invalid input. Please enter a number.")
        else:
            num_ingredients = int(num_ingredients_input)
            if num_ingredients > 0:
                break
            else:
                print("Please enter at least 1 ingredient.")
                
    print("\nEnter your ingredients:")
    for i in range(num_ingredients):
        ingredient = input(f"Ingredient {i+1}: ").strip()
        while not ingredient:
            print("Ingredient cannot be empty.")
            ingredient = input(f"Ingredient {i+1}: ").strip()
        ingredients.append(ingredient)
        
    # Convert ingredients list to comma-separated string using join()
    ingredients_str = ", ".join(ingredients)
    
    # Create new Recipe object called recipe_entry
    recipe_entry = Recipe(
        name=name,
        ingredients=ingredients_str,
        cooking_time=cooking_time
    )
    
    # Generate difficulty by calling calculate_difficulty()
    recipe_entry.calculate_difficulty()
    
    # Add to session and commit
    session.add(recipe_entry)
    session.commit()
    
    print(f"\n✓ Recipe '{name}' added successfully!")
    print(f"  Difficulty: {recipe_entry.difficulty}")
    
def view_all_recipes():
    """Display all recipes in the database."""
    print("\n" + "="*50)
    print("ALL RECIPES")
    print("="*50)
    
    # Retrieve all recipes as a list
    recipes = session.query(Recipe).all()
    
    # Check if there are any entries
    if not recipes:
        print("\nNo recipes found in the database.")
        return None
        
    print(f"\nTotal recipes: {len(recipes)}\n")
    
    # Loop through and display each recipe using __str__
    for recipe in recipes:
        print(recipe)
        
def search_by_ingredient():
    """Search for recipes by ingredient."""
    print("\n" + "="*50)
    print("SEARCH RECIPES BY INGREDIENT")
    print("="*50)
    
    # Check if table has any entries using count()
    if session.query(Recipe).count() == 0:
        print("\nNo recipes found in the database.")
        return None
        
    # Retrieve only the ingredients column
    results = session.query(Recipe.ingredients).all()
    
    # Initialize empty list for all ingredients
    all_ingredients = []
    
    # Go through each entry and build all_ingredients list
    for result in results:
        ingredients_list = result[0].split(", ")
        for ingredient in ingredients_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
                
    # Display ingredients with numbers
    print("\nAvailable ingredients:")
    for i, ingredient in enumerate(all_ingredients, 1):
        print(f"{i}. {ingredient}")
        
    # Get user's selection
    print("\nEnter the numbers of ingredients to search for, separated by spaces:")
    user_input = input("Your choice: ").strip()
    
    # Validate input
    try:
        selected_numbers = [int(num) for num in user_input.split()]
    except ValueError:
        print("\nInvalid input. Please enter numbers only.")
        return None
        
    # Check that selections are valid
    for num in selected_numbers:
        if num < 1 or num > len(all_ingredients):
            print(f"\nInvalid selection: {num}. Please choose numbers between 1 and {len(all_ingredients)}.")
            return None
            
    # Create search_ingredients list based on selection
    search_ingredients = [all_ingredients[num - 1] for num in selected_numbers]
    
    # Initialize conditions list
    conditions = []
    
    # Build like conditions for each search ingredient
    for ingredient in search_ingredients:
        like_term = f"%{ingredient}%"
        conditions.append(Recipe.ingredients.like(like_term))
        
    # Retrieve recipes using filter with conditions
    print(f"\n{'='*50}")
    print(f"Recipes containing: {', '.join(search_ingredients)}")
    print("="*50)
    
    # Use filter with all conditions (AND logic)
    recipes = session.query(Recipe).filter(*conditions).all()
    
    if recipes:
        for recipe in recipes:
            print(recipe)
    else:
        print(f"\nNo recipes found containing all specified ingredients.")

def edit_recipe():
    """Update an existing recipe in the database."""
    print("\n" + "="*50)
    print("UPDATE RECIPE")
    print("="*50)
    
    # Check if any recipes exist
    if session.query(Recipe).count() == 0:
        print("\nNo recipes found in the database.")
        return None
        
    # Retrieve id and name for each recipe
    results = session.query(Recipe.id, Recipe.name).all()
    
    # Display recipes available to user
    print("\nAvailable recipes:")
    for recipe_id, recipe_name in results:
        print(f"{recipe_id}. {recipe_name}")
        
    # Get recipe ID to update
    recipe_id_input = input("\nEnter the ID of the recipe to update: ").strip()
    
    # Validate input
    if not recipe_id_input.isnumeric():
        print("\nInvalid input. Please enter a number.")
        return None
        
    recipe_id = int(recipe_id_input)
    
    # Retrieve the entire recipe into recipe_to_edit
    recipe_to_edit = session.query(Recipe).filter(Recipe.id == recipe_id).first()
    
    if not recipe_to_edit:
        print("\nRecipe not found.")
        return None
        
    # Display recipe with only name, ingredients, and cooking_time
    print(f"\nRecipe to edit:")
    print(f"1. Name: {recipe_to_edit.name}")
    print(f"2. Ingredients: {recipe_to_edit.ingredients}")
    print(f"3. Cooking Time: {recipe_to_edit.cooking_time} minutes")
    
    # Ask which attribute to edit
    print("\nWhich attribute would you like to edit?")
    attribute_choice = input("Enter 1 (Name), 2 (Ingredients), or 3 (Cooking Time): ").strip()
    
    # Check user input
    if attribute_choice not in ['1', '2', '3']:
        print("\nInvalid choice. No changes made.")
        return None
        
    # Edit based on choice using if-else statements
    if attribute_choice == "1":
        new_name = input("Enter new name: ").strip()
        if len(new_name) == 0:
            print("Name cannot be empty.")
            return None
        if len(new_name) > 50:
            print("Recipe name too long! Maximum 50 characters.")
            return None
        recipe_to_edit.name = new_name
        print(f"\n✓ Recipe name updated to '{new_name}'")
        
    elif attribute_choice == "2":
        # Collect ingredients using for loop
        while True:
            num_ingredients_input = input("\nHow many ingredients would you like to enter? ").strip()
            if not num_ingredients_input.isnumeric():
                print("Invalid input. Please enter a number.")
            else:
                num_ingredients = int(num_ingredients_input)
                if num_ingredients > 0:
                    break
                else:
                    print("Please enter at least 1 ingredient.")
                    
        ingredients = []
        print("\nEnter your ingredients:")
        for i in range(num_ingredients):
            ingredient = input(f"Ingredient {i+1}: ").strip()
            while not ingredient:
                print("Ingredient cannot be empty.")
                ingredient = input(f"Ingredient {i+1}: ").strip()
            ingredients.append(ingredient)
            
        recipe_to_edit.ingredients = ", ".join(ingredients)
        recipe_to_edit.calculate_difficulty()
        print(f"\n✓ Ingredients updated. New difficulty: {recipe_to_edit.difficulty}")
        
    else:  # attribute_choice == "3"
        cooking_time_input = input("Enter new cooking time (in minutes): ").strip()
        if not cooking_time_input.isnumeric():
            print("Invalid input. Cooking time must be a number.")
            return None
            
        new_time = int(cooking_time_input)
        if new_time <= 0:
            print("Cooking time must be positive.")
            return None
            
        recipe_to_edit.cooking_time = new_time
        recipe_to_edit.calculate_difficulty()
        print(f"\n✓ Cooking time updated to {new_time} minutes. New difficulty: {recipe_to_edit.difficulty}")
        
    # Commit changes
    session.commit()

def delete_recipe():
    """Delete a recipe from the database."""
    print("\n" + "="*50)
    print("DELETE RECIPE")
    print("="*50)
    
    # Check if any recipes exist
    if session.query(Recipe).count() == 0:
        print("\nNo recipes found in the database.")
        return None
        
    # Retrieve id and name of every recipe
    results = session.query(Recipe.id, Recipe.name).all()
    
    # List recipes to user
    print("\nAvailable recipes:")
    for recipe_id, recipe_name in results:
        print(f"{recipe_id}. {recipe_name}")
        
    # Ask which recipe to delete
    recipe_id_input = input("\nEnter the ID of the recipe to delete: ").strip()
    
    # Verify input
    if not recipe_id_input.isnumeric():
        print("\nInvalid input. Please enter a number.")
        return None
        
    recipe_id = int(recipe_id_input)
    
    # Retrieve the corresponding object
    recipe_to_delete = session.query(Recipe).filter(Recipe.id == recipe_id).first()
    
    if not recipe_to_delete:
        print("\nRecipe not found.")
        return None
        
    # Ask for confirmation
    recipe_name = recipe_to_delete.name
    confirm = input(f"\nAre you sure you want to delete '{recipe_name}'? (yes/no): ").strip().lower()
    
    # Perform delete if confirmed
    if confirm == 'yes':
        session.delete(recipe_to_delete)
        session.commit()
        print(f"\n✓ Recipe '{recipe_name}' deleted successfully!")
    else:
        print("\nDeletion cancelled.")
        return None

# --------------------------------------------------------------------------
# --- Main Execution Block (Updated/Implemented) ---
# --------------------------------------------------------------------------

if __name__ == "__main__":
    print("\n" + "="*50)
    print("Welcome to the Recipe App!")
    print("="*50)
    
    # This block ensures the database connection is tested before the menu starts
    try:
        engine.connect()
        print("\nDatabase connection established.")
        print(f"Connected to: {DATABASE}")
        
        main_menu()
        
    except Exception as e:
        print("\n🛑 ERROR: Could not connect to the database.")
        print("Please ensure your MySQL server is running and credentials are correct.")
        # print(f"Details: {e}") # Uncomment for debugging details