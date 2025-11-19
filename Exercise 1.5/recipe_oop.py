class Recipe:
    """A class to represent a cooking recipe with automatic difficulty calculation."""
    
    # Class variable to store all unique ingredients across all recipes
    all_ingredients = []
    
    def __init__(self, name):
        """
        Initialize a Recipe object.
        
        Args:
            name (str): The name of the recipe
        """
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = None
    
    def get_name(self):
        """
        Getter method for recipe name.
        
        Returns:
            str: The recipe name
        """
        return self.name
    
    def set_name(self, name):
        """
        Setter method for recipe name.
        
        Args:
            name (str): The new name for the recipe
        """
        self.name = name
    
    def get_cooking_time(self):
        """
        Getter method for cooking time.
        
        Returns:
            int: The cooking time in minutes
        """
        return self.cooking_time
    
    def set_cooking_time(self, cooking_time):
        """
        Setter method for cooking time.
        
        Args:
            cooking_time (int): The cooking time in minutes
        """
        self.cooking_time = cooking_time
    
    def add_ingredients(self, *ingredients):
        """
        Add variable-length ingredients to the recipe.
        
        Args:
            *ingredients: Variable number of ingredient strings
        """
        for ingredient in ingredients:
            self.ingredients.append(ingredient)
        self.update_all_ingredients()
    
    def get_ingredients(self):
        """
        Getter method for ingredients.
        
        Returns:
            list: The list of ingredients
        """
        return self.ingredients
    
    def calculate_difficulty(self):
        """
        Calculate and set the difficulty level based on cooking time and number of ingredients.
        
        Difficulty levels:
        - Easy: cooking_time < 10 and ingredients < 4
        - Medium: cooking_time < 10 and ingredients >= 4
        - Intermediate: cooking_time >= 10 and ingredients < 4
        - Hard: cooking_time >= 10 and ingredients >= 4
        """
        num_ingredients = len(self.ingredients)
        
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
    
    def get_difficulty(self):
        """
        Getter method for difficulty. Calculates difficulty if not yet set.
        
        Returns:
            str: The difficulty level
        """
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty
    
    def search_ingredient(self, ingredient):
        """
        Search for a specific ingredient in the recipe.
        
        Args:
            ingredient (str): The ingredient to search for
            
        Returns:
            bool: True if ingredient is found, False otherwise
        """
        return ingredient in self.ingredients
    
    def update_all_ingredients(self):
        """
        Update the class variable all_ingredients with ingredients from this recipe.
        Only adds ingredients that aren't already present.
        """
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)
    
    def __str__(self):
        """
        Return a formatted string representation of the recipe.
        
        Returns:
            str: A well-formatted string containing all recipe details
        """
        output = f"\nRecipe: {self.name}\n"
        output += f"Cooking Time: {self.cooking_time} minutes\n"
        output += f"Difficulty: {self.get_difficulty()}\n"
        output += "Ingredients:\n"
        for ingredient in self.ingredients:
            output += f"  - {ingredient}\n"
        return output
    
    def recipe_search(data, search_term):
        """
        Search for recipes containing a specific ingredient.
        
        Args:
            data (list): List of Recipe objects to search from
            search_term (str): The ingredient to be searched for
        """
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)
    
    def recipe_search(data, search_term):
        """
        Search for recipes containing a specific ingredient.
        
        Args:
            data (list): List of Recipe objects to search through
            search_term (str): The ingredient to search for
        """
        print(f"\nRecipes containing '{search_term}':")
        print("-" * 50)
        found = False
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)
                found = True
        
        if not found:
            print(f"No recipes found containing '{search_term}'")


# Example usage and testing
if __name__ == "__main__":
    # Create a tea recipe object
    tea = Recipe("Tea")
    tea.add_ingredients("Tea Leaves", "Sugar", "Water")
    tea.set_cooking_time(5)
    print(tea)
    
    coffee = Recipe("Coffee")
    coffee.set_cooking_time(5)
    coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
    print(coffee)
    
    cake = Recipe("Cake")
    cake.set_cooking_time(50)
    cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
    print(cake)
    
    banana_smoothie = Recipe("Banana Smoothie")
    banana_smoothie.set_cooking_time(5)
    banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
    print(banana_smoothie)
    
    # Create a list of recipes
    recipes_list = [tea, coffee, cake, banana_smoothie]
    
    # Display all ingredients used across all recipes
    print("\n" + "="*50)
    print("All ingredients used in recipes:")
    print("="*50)
    for ingredient in Recipe.all_ingredients:
        print(f"  - {ingredient}")
    
    # Search for recipes by ingredient
    print("\n" + "="*50)
    Recipe.recipe_search(recipes_list, "Water")
    Recipe.recipe_search(recipes_list, "Sugar")
    Recipe.recipe_search(recipes_list, "Bananas")