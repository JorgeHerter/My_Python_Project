# Recipe App - MySQL Database Edition

A command-line Python application that manages recipes using a MySQL database. This app allows you to create, search, update, and delete recipes with automatic difficulty calculation based on cooking time and ingredient count.

## Features

- **Create Recipes**: Add new recipes with name, cooking time, and ingredients
- **Search by Ingredient**: Find recipes containing specific ingredients
- **Update Recipes**: Modify existing recipe details (name, cooking time, or ingredients)
- **Delete Recipes**: Remove recipes from the database
- **Automatic Difficulty Calculation**: Recipes are categorized as Easy, Medium, Intermediate, or Hard
- **MySQL Database Storage**: All recipes stored persistently in MySQL database
- **Ingredient Tracking**: View all available ingredients across all recipes

## Difficulty Levels

The app automatically calculates recipe difficulty based on the following criteria:

| Difficulty | Cooking Time | Number of Ingredients |
|------------|--------------|----------------------|
| **Easy** | < 10 minutes | < 4 ingredients |
| **Medium** | < 10 minutes | ≥ 4 ingredients |
| **Intermediate** | ≥ 10 minutes | < 4 ingredients |
| **Hard** | ≥ 10 minutes | ≥ 4 ingredients |

## Prerequisites

- Python 3.x
- MySQL Server (or MariaDB via XAMPP)
- `mysql-connector-python` package

## Installation

### 1. Install MySQL/MariaDB

**Option A: Using XAMPP (Recommended for beginners)**
1. Download XAMPP from https://www.apachefriends.org/
2. Install XAMPP and start the MySQL service from XAMPP Control Panel

**Option B: Using MySQL Server**
1. Download MySQL Community Server from https://dev.mysql.com/downloads/mysql/
2. Install and start the MySQL service

### 2. Create MySQL User

Open MySQL command line:
```bash
# For XAMPP
C:\xampp\mysql\bin\mysql.exe -u root -p

# For standard MySQL
mysql -u root -p
```

Create the user and grant privileges:
```sql
CREATE USER 'cf-python'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'cf-python'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### 3. Install Python Dependencies

```bash
pip install mysql-connector-python
```

### 4. Download the Script

Save `recipe_mysql.py` to your project directory.

## Database Structure

The application automatically creates:

**Database**: `task_database`

**Table**: `Recipes`

| Column | Type | Description |
|--------|------|-------------|
| `id` | INT (Primary Key, Auto-increment) | Unique recipe identifier |
| `name` | VARCHAR(50) | Recipe name |
| `ingredients` | VARCHAR(255) | Comma-separated ingredient list |
| `cooking_time` | INT | Cooking time in minutes |
| `difficulty` | VARCHAR(20) | Auto-calculated difficulty level |

## Usage

### Running the Application

```bash
python recipe_mysql.py
```

Or in IPython:
```python
run "recipe_mysql.py"
```

### Main Menu

```
Main Menu:
==================================================
1. Create a new recipe
2. Search for recipes by ingredient
3. Update an existing recipe
4. Delete a recipe
Type 'quit' to exit the program
==================================================
```

## Operations Guide

### 1. Create a New Recipe

Select option `1` from the main menu.

**Example:**
```
Enter recipe name: Tea
Enter cooking time (in minutes): 5
Enter ingredients (type 'done' when finished):
Ingredient: Tea Leaves
Ingredient: Sugar
Ingredient: Water
Ingredient: done

✓ Recipe 'Tea' added successfully!
  Difficulty: Easy
```

**Features:**
- Input validation for cooking time (must be positive integer)
- Multiple ingredients support
- Automatic difficulty calculation
- Ingredients stored as comma-separated string

### 2. Search for Recipes by Ingredient

Select option `2` from the main menu.

**Process:**
1. View all available ingredients with numbers
2. Select ingredient by number
3. View all recipes containing that ingredient

**Example:**
```
Available ingredients:
1. Bananas
2. Butter
3. Coffee Powder
4. Sugar
5. Water

Enter the number of the ingredient to search: 5

Recipes containing 'Water':
==================================================
ID: 1
Name: Tea
Ingredients: Tea Leaves, Sugar, Water
Cooking Time: 5 minutes
Difficulty: Easy
```

**Search Logic:**
- Uses SQL `LIKE` operator with wildcard pattern `%ingredient%`
- Finds ingredients at beginning, middle, or end of string
- Case-insensitive search

### 3. Update an Existing Recipe

Select option `3` from the main menu.

**Process:**
1. View all recipes with IDs
2. Select recipe to update by ID
3. Choose field to update (name, ingredients, or cooking time)
4. Enter new value
5. Difficulty automatically recalculated if needed

**Example:**
```
Available recipes:
1. Tea
2. Coffee
3. Cake

Enter the ID of the recipe to update: 1

Current recipe details:
1. Name: Tea
2. Ingredients: Tea Leaves, Sugar, Water
3. Cooking Time: 5 minutes

Which field would you like to update?
Enter 1 (Name), 2 (Ingredients), or 3 (Cooking Time): 3
Enter new cooking time (in minutes): 15

✓ Cooking time updated to 15 minutes. New difficulty: Intermediate
```

**Auto-Recalculation:**
- Updating cooking time → recalculates difficulty
- Updating ingredients → recalculates difficulty
- Updating name → no difficulty change

### 4. Delete a Recipe

Select option `4` from the main menu.

**Process:**
1. View all recipes with IDs
2. Select recipe to delete by ID
3. Confirm deletion
4. Recipe removed from database

**Example:**
```
Available recipes:
1. Tea
2. Coffee
3. Cake

Enter the ID of the recipe to delete: 2
Are you sure you want to delete 'Coffee'? (yes/no): yes

✓ Recipe 'Coffee' deleted successfully!
```

**Safety Features:**
- Confirmation required before deletion
- Type 'yes' to confirm, anything else cancels
- No undo available - deletion is permanent

### 5. Exit the Program

Type `quit` at the main menu to exit.

**What happens:**
- All changes are automatically committed
- Database connection is closed
- Program exits gracefully

## Code Structure

### Main Functions

#### `main()`
- Establishes MySQL connection
- Creates database and table if they don't exist
- Runs the main menu loop
- Handles user input and function calls
- Closes connection on exit

#### `create_recipe(conn, cursor)`
- Collects recipe details from user
- Validates input (cooking time must be positive)
- Converts ingredient list to comma-separated string using `join()`
- Calculates difficulty
- Inserts recipe into database

#### `search_recipe(conn, cursor)`
- Retrieves all ingredients from database
- Removes duplicates and sorts alphabetically
- User selects ingredient by number
- Searches using SQL `LIKE %ingredient%` pattern
- Displays matching recipes

#### `update_recipe(conn, cursor)`
- Lists all recipes with IDs
- User selects recipe and field to update
- Collects new value from user
- Recalculates difficulty if cooking_time or ingredients changed
- Updates database with new values

#### `delete_recipe(conn, cursor)`
- Lists all recipes with IDs
- User selects recipe by ID
- Asks for confirmation
- Deletes recipe from database

#### `calculate_difficulty(cooking_time, num_ingredients)`
- Takes cooking time and ingredient count as parameters
- Returns difficulty string based on criteria
- Used by create and update functions

## Technical Details

### Ingredient Storage

Since MySQL doesn't fully support array data types, ingredients are stored as comma-separated strings:

**Storage Format:**
```
"Tea Leaves, Sugar, Water"
```

**Conversion Methods:**
- **List to String**: `", ".join(ingredients_list)`
- **String to List**: `ingredients_string.split(", ")`

### SQL Queries Used

**Create Database:**
```sql
CREATE DATABASE IF NOT EXISTS task_database
```

**Create Table:**
```sql
CREATE TABLE IF NOT EXISTS Recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
)
```

**Insert Recipe:**
```sql
INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) 
VALUES (%s, %s, %s, %s)
```

**Search by Ingredient:**
```sql
SELECT * FROM Recipes WHERE ingredients LIKE %s
```

**Update Recipe:**
```sql
UPDATE Recipes SET <column> = %s WHERE id = %s
```

**Delete Recipe:**
```sql
DELETE FROM Recipes WHERE id = %s
```

### Error Handling

- **Input Validation**: Cooking time must be positive integer
- **Database Errors**: Wrapped in try-catch (can be enhanced)
- **Empty Results**: Friendly messages when no recipes found
- **User Confirmation**: Required for destructive operations (delete)

## Configuration

### Database Connection Settings

Edit these values in `recipe_mysql.py` if your MySQL setup is different:

```python
conn = mysql.connector.connect(
    host='localhost',      # MySQL server address
    user='cf-python',      # Your MySQL username
    passwd='password'      # Your MySQL password
)
```

### XAMPP Default Settings

If using XAMPP with default settings:
```python
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=''  # Empty password
)
```

## Example Recipes

Here are some sample recipes you can create to test the app:

### Tea (Easy)
- Cooking Time: 5 minutes
- Ingredients: Tea Leaves, Sugar, Water

### Coffee (Easy)
- Cooking Time: 5 minutes
- Ingredients: Coffee Powder, Sugar, Water

### Cake (Hard)
- Cooking Time: 50 minutes
- Ingredients: Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk

### Banana Smoothie (Medium)
- Cooking Time: 5 minutes
- Ingredients: Bananas, Milk, Peanut Butter, Sugar, Ice Cubes

## Troubleshooting

### Connection Errors

**Error: "Can't connect to MySQL server"**
- Ensure MySQL/XAMPP is running
- Check that MySQL service is started
- Verify host, username, and password

**Error: "Access denied for user"**
- Verify user 'cf-python' exists with correct password
- Run user creation commands again
- Check that privileges are granted

### Module Not Found

**Error: "No module named 'mysql'"**
```bash
pip install mysql-connector-python
```

### Database Issues

**Table doesn't exist:**
- The script auto-creates the database and table
- If issues persist, manually create using the SQL in Technical Details section

**Can't see data:**
- Use phpMyAdmin (http://localhost/phpmyadmin) to view data
- Or use MySQL command line: `USE task_database; SELECT * FROM Recipes;`

## Project Structure

```
recipe-mysql-app/
│
├── recipe_mysql.py        # Main application file
└── README.md              # This file
```

## Learning Objectives

This project demonstrates:
- MySQL database integration with Python
- CRUD operations (Create, Read, Update, Delete)
- SQL query building and parameterization
- User input validation
- Command-line interface design
- Data type conversion (list ↔ string)
- Conditional logic for calculations
- Error handling and user feedback

## Differences from OOP Version

| Feature | OOP Version | MySQL Version |
|---------|------------|---------------|
| **Storage** | In-memory objects | MySQL database |
| **Persistence** | Lost on exit | Permanent storage |
| **Ingredients** | Python list | Comma-separated string |
| **Search** | Method on Recipe class | SQL LIKE query |
| **Data Access** | Object attributes | SQL SELECT queries |

## Future Enhancements

Potential improvements:
- [ ] Recipe categories (breakfast, lunch, dinner, dessert)
- [ ] Serving size tracking
- [ ] Nutritional information
- [ ] Recipe ratings and reviews
- [ ] Export recipes to PDF/text file
- [ ] Import recipes from file
- [ ] Recipe images (stored as BLOB)
- [ ] User authentication system
- [ ] Advanced search (multiple ingredients, time range)
- [ ] Recipe sharing between users

## Security Notes

⚠️ **Important**: This application is designed for educational purposes. For production use:
- Use environment variables for database credentials
- Implement proper password hashing
- Add SQL injection protection (currently using parameterized queries ✓)
- Add user authentication
- Implement input sanitization
- Add comprehensive error handling
- Use connection pooling for better performance

## License

This project is created for educational purposes as part of a Python programming course.

## Author

Created as part of Career Foundry's Python course, demonstrating MySQL database integration with Python applications.

## Support

For issues or questions:
- Check the Troubleshooting section
- Review MySQL/MariaDB documentation
- Verify all prerequisites are installed
- Ensure MySQL service is running

---

**Version**: 1.0  
**Last Updated**: November 2024  
**Python Version**: 3.x  
**MySQL Connector Version**: 9.5.0