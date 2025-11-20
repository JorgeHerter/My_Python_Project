Recipe App – SQLAlchemy CRUD Application

This project is a command-line Recipe Management Application built using Python, MySQL, and SQLAlchemy (ORM).
The app allows users to create, view, search, edit, and delete recipe entries stored in a MySQL database.

📦 Features
1. Create Recipes

Enter recipe name, ingredients, and cooking time

Automatic difficulty calculation

Input validation for name, ingredients, and numeric fields

2. View All Recipes

Displays all recipes in a clean, formatted output using __str__

Alerts user if no recipes exist

3. Search Recipes by Ingredients

Collects all unique ingredients from the database

Users select ingredients by number (supports multi-ingredient search)

Retrieves and displays matching recipes

4. Edit Recipes

User selects a recipe by its ID

Editable fields: name, ingredients, and cooking_time

Difficulty recalculated after edits

5. Delete Recipes

User selects recipe by its ID

Confirmation step before deletion

6. Interactive Main Menu

Looped menu navigation

Quit option safely closes database session and engine connection

🗂 Project Structure
project/
│
├── recipe_app.py        # Main application script
└── README.md

⚙️ Requirements

Install all dependencies using:

pip install sqlalchemy mysql-connector-python

Your MySQL server must be running, and you need:

username

password

host

database name

These credentials are used to build the SQLAlchemy engine:

engine = create_engine("mysql+mysqlconnector://<username>:<password>@<host>/<database>")

📜 What the Script Does
1. SQLAlchemy Setup

Creates engine

Generates session factory

Initializes a session for CRUD operations

2. Model Definition

Recipe model includes:

id (PK, autoincrement)

name (String 50)

ingredients (String 255)

cooking_time (Integer)

difficulty (String 20)

calculate_difficulty()

return_ingredients_as_list()

Custom __repr__ and __str__ methods

3. Database Table Creation

Runs Base.metadata.create_all(engine) to set up the final_recipes table

4. CRUD Functions

Functions implemented:

create_recipe()

view_all_recipes()

search_by_ingredients()

edit_recipe()

delete_recipe()

5. Main Menu Loop

Menu options call the above functions until the user types quit.
Session and engine are then properly closed.

▶️ Running the Application

From your terminal:

python recipe_app.py


Follow the on-screen menu to manage recipes.

🧪 Difficulty Calculation Logic

Difficulty is automatically computed using:

The number of ingredients

The cooking time (in minutes)

You may customize the thresholds based on prior exercise rules.

📌 Notes

The ingredients string is stored as:
ingredient1, ingredient2, ingredient3

The search uses SQL LIKE expressions to find matches.

Input validation ensures clean data entry and prevents common errors.

📖 Example Menu
What would you like to do?

1. Create a new recipe
2. View all recipes
3. Search recipes by ingredients
4. Edit a recipe
5. Delete a recipe
Type 'quit' to exit.
