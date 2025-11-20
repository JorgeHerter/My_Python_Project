import mysql.connector

# Part 1: Create & Connect Database

def main():
    """Main function to run the Recipe MySQL application."""
    
    # Initialize connection object with specified parameters
    conn = mysql.connector.connect(
        host='localhost',
        user='cf-python',
        passwd='password'
    )
    
    # Create a cursor object
    cursor = conn.cursor()
    
    # Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
    
    # Use the database
    cursor.execute("USE task_database")
    
    # Create Recipes table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Recipes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            ingredients VARCHAR(255),
            cooking_time INT,
            difficulty VARCHAR(20)
        )
    ''')
    
    print("Database and table setup complete!")
    print("\nWelcome to the Recipe Management System")
    print("=" * 50)
    
    # Main menu loop
    choice = ""
    while choice != "quit":
        print("\nMain Menu:")
        print("=" * 50)
        print("1. Create a new recipe")
        print("2. Search for recipes by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("Type 'quit' to exit the program")
        print("=" * 50)
        
        choice = input("\nYour choice: ").strip().lower()
        
        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "quit":
            print("\nClosing the application. Goodbye!")
        else:
            print("\nInvalid choice. Please try again.")
    
    # Close connection
    conn.close()


def create_recipe(conn, cursor):
    """Create a new recipe and add it to the database."""
    print("\n" + "=" * 50)
    print("CREATE NEW RECIPE")
    print("=" * 50)
    
    # Get recipe name
    name = input("\nEnter recipe name: ").strip()
    
    # Get cooking time
    while True:
        try:
            cooking_time = int(input("Enter cooking time (in minutes): "))
            if cooking_time > 0:
                break
            else:
                print("Cooking time must be positive. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Get ingredients
    ingredients = []
    print("\nEnter ingredients (type 'done' when finished):")
    while True:
        ingredient = input("Ingredient: ").strip()
        if ingredient.lower() == 'done':
            if len(ingredients) > 0:
                break
            else:
                print("Please add at least one ingredient.")
        elif ingredient:
            ingredients.append(ingredient)
    
    # Convert ingredients list to comma-separated string
    ingredients_str = ", ".join(ingredients)
    
    # Calculate difficulty
    difficulty = calculate_difficulty(cooking_time, len(ingredients))
    
    # Insert into database
    sql = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    val = (name, ingredients_str, cooking_time, difficulty)
    
    cursor.execute(sql, val)
    conn.commit()
    
    print(f"\n✓ Recipe '{name}' added successfully!")
    print(f"  Difficulty: {difficulty}")


def search_recipe(conn, cursor):
    """Search for recipes by ingredient."""
    print("\n" + "=" * 50)
    print("SEARCH RECIPES BY INGREDIENT")
    print("=" * 50)
    
    # Get all ingredients from database
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    
    if not results:
        print("\nNo recipes found in the database.")
        return
    
    # Collect all unique ingredients
    all_ingredients = set()
    for row in results:
        ingredients_list = row[0].split(", ")
        all_ingredients.update(ingredients_list)
    
    # Display available ingredients
    all_ingredients = sorted(list(all_ingredients))
    print("\nAvailable ingredients:")
    for i, ingredient in enumerate(all_ingredients, 1):
        print(f"{i}. {ingredient}")
    
    # Get user choice
    while True:
        try:
            choice = int(input("\nEnter the number of the ingredient to search: "))
            if 1 <= choice <= len(all_ingredients):
                search_ingredient = all_ingredients[choice - 1]
                break
            else:
                print(f"Please enter a number between 1 and {len(all_ingredients)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Search for recipes containing the ingredient
    print(f"\n{'=' * 50}")
    print(f"Recipes containing '{search_ingredient}':")
    print("=" * 50)
    
    cursor.execute("SELECT * FROM Recipes WHERE ingredients LIKE %s", ('%' + search_ingredient + '%',))
    results = cursor.fetchall()
    
    if results:
        for row in results:
            print(f"\nID: {row[0]}")
            print(f"Name: {row[1]}")
            print(f"Ingredients: {row[2]}")
            print(f"Cooking Time: {row[3]} minutes")
            print(f"Difficulty: {row[4]}")
    else:
        print(f"\nNo recipes found containing '{search_ingredient}'.")


def update_recipe(conn, cursor):
    """Update an existing recipe in the database."""
    print("\n" + "=" * 50)
    print("UPDATE RECIPE")
    print("=" * 50)
    
    # Display all recipes
    cursor.execute("SELECT id, name FROM Recipes")
    results = cursor.fetchall()
    
    if not results:
        print("\nNo recipes found in the database.")
        return
    
    print("\nAvailable recipes:")
    for row in results:
        print(f"{row[0]}. {row[1]}")
    
    # Get recipe ID to update
    while True:
        try:
            recipe_id = int(input("\nEnter the ID of the recipe to update: "))
            cursor.execute("SELECT * FROM Recipes WHERE id = %s", (recipe_id,))
            recipe = cursor.fetchone()
            if recipe:
                break
            else:
                print("Recipe not found. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Display current recipe details
    print(f"\nCurrent recipe details:")
    print(f"1. Name: {recipe[1]}")
    print(f"2. Ingredients: {recipe[2]}")
    print(f"3. Cooking Time: {recipe[3]} minutes")
    
    # Get field to update
    print("\nWhich field would you like to update?")
    field_choice = input("Enter 1 (Name), 2 (Ingredients), or 3 (Cooking Time): ").strip()
    
    if field_choice == "1":
        new_name = input("Enter new name: ").strip()
        cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s", (new_name, recipe_id))
        print(f"\n✓ Recipe name updated to '{new_name}'")
    
    elif field_choice == "2":
        ingredients = []
        print("\nEnter new ingredients (type 'done' when finished):")
        while True:
            ingredient = input("Ingredient: ").strip()
            if ingredient.lower() == 'done':
                if len(ingredients) > 0:
                    break
                else:
                    print("Please add at least one ingredient.")
            elif ingredient:
                ingredients.append(ingredient)
        
        ingredients_str = ", ".join(ingredients)
        difficulty = calculate_difficulty(recipe[3], len(ingredients))
        cursor.execute("UPDATE Recipes SET ingredients = %s, difficulty = %s WHERE id = %s", 
                      (ingredients_str, difficulty, recipe_id))
        print(f"\n✓ Ingredients updated. New difficulty: {difficulty}")
    
    elif field_choice == "3":
        while True:
            try:
                new_time = int(input("Enter new cooking time (in minutes): "))
                if new_time > 0:
                    break
                else:
                    print("Cooking time must be positive. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Recalculate difficulty
        ingredients_list = recipe[2].split(", ")
        difficulty = calculate_difficulty(new_time, len(ingredients_list))
        cursor.execute("UPDATE Recipes SET cooking_time = %s, difficulty = %s WHERE id = %s", 
                      (new_time, difficulty, recipe_id))
        print(f"\n✓ Cooking time updated to {new_time} minutes. New difficulty: {difficulty}")
    
    else:
        print("\nInvalid choice. No changes made.")
        return
    
    conn.commit()


def delete_recipe(conn, cursor):
    """Delete a recipe from the database."""
    print("\n" + "=" * 50)
    print("DELETE RECIPE")
    print("=" * 50)
    
    # Display all recipes
    cursor.execute("SELECT id, name FROM Recipes")
    results = cursor.fetchall()
    
    if not results:
        print("\nNo recipes found in the database.")
        return
    
    print("\nAvailable recipes:")
    for row in results:
        print(f"{row[0]}. {row[1]}")
    
    # Get recipe ID to delete
    while True:
        try:
            recipe_id = int(input("\nEnter the ID of the recipe to delete: "))
            cursor.execute("SELECT name FROM Recipes WHERE id = %s", (recipe_id,))
            recipe = cursor.fetchone()
            if recipe:
                recipe_name = recipe[0]
                break
            else:
                print("Recipe not found. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Confirm deletion
    confirm = input(f"\nAre you sure you want to delete '{recipe_name}'? (yes/no): ").strip().lower()
    
    if confirm == 'yes':
        cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))
        conn.commit()
        print(f"\n✓ Recipe '{recipe_name}' deleted successfully!")
    else:
        print("\nDeletion cancelled.")


def calculate_difficulty(cooking_time, num_ingredients):
    """
    Calculate recipe difficulty based on cooking time and number of ingredients.
    
    Args:
        cooking_time (int): Time in minutes
        num_ingredients (int): Number of ingredients
        
    Returns:
        str: Difficulty level (Easy, Medium, Intermediate, Hard)
    """
    if cooking_time < 10:
        if num_ingredients < 4:
            return "Easy"
        else:
            return "Medium"
    else:
        if num_ingredients < 4:
            return "Intermediate"
        else:
            return "Hard"


if __name__ == "__main__":
    main()