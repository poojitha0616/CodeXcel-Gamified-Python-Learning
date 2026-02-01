"""
Script to add more Python learning modules and challenges to CodeXcel
Run this to populate the database with additional content
"""

from pymongo import MongoClient
from bson.objectid import ObjectId
import os

# MongoDB connection - use environment variable or localhost
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')

print(f"Connecting to MongoDB...")
client = MongoClient(MONGO_URI)
db = client.codexcel

# Collections
modules_collection = db.modules
challenges_collection = db.challenges

def add_modules_and_challenges():
    """Add new modules with challenges"""
    
    # Module 3: Data Structures
    print("Adding Module 3: Data Structures...")
    
    # Create challenges for Module 3
    challenge_3_1 = challenges_collection.insert_one({
        'title': 'Working with Lists',
        'description': 'Create and manipulate a list of numbers. Print the sum of all elements.',
        'xp_reward': 50,
        'difficulty': 'Easy',
        'input_description': 'Create a list: [10, 20, 30, 40, 50]',
        'output': '150',
        'hints': [
            'Use the sum() function',
            'Store the list in a variable',
            'Print the result'
        ]
    }).inserted_id
    
    challenge_3_2 = challenges_collection.insert_one({
        'title': 'List Indexing',
        'description': 'Access the third element of the list [5, 10, 15, 20, 25] and print it.',
        'xp_reward': 50,
        'difficulty': 'Easy',
        'input_description': 'List: [5, 10, 15, 20, 25]',
        'output': '15',
        'hints': [
            'List indexing starts at 0',
            'Third element is at index 2',
            'Use square brackets []'
        ]
    }).inserted_id
    
    challenge_3_3 = challenges_collection.insert_one({
        'title': 'Dictionary Basics',
        'description': 'Create a dictionary with keys "name" and "age". Access and print the value of "name".',
        'xp_reward': 50,
        'difficulty': 'Easy',
        'input_description': 'Dictionary: {"name": "Python", "age": 32}',
        'output': 'Python',
        'hints': [
            'Use curly braces {} for dictionaries',
            'Access values using keys',
            'Use square brackets or .get()'
        ]
    }).inserted_id
    
    challenge_3_4 = challenges_collection.insert_one({
        'title': 'Tuple Operations',
        'description': 'Create a tuple (1, 2, 3, 4, 5) and print its length.',
        'xp_reward': 50,
        'difficulty': 'Easy',
        'input_description': 'Tuple: (1, 2, 3, 4, 5)',
        'output': '5',
        'hints': [
            'Use parentheses () for tuples',
            'Use len() function',
            'Tuples are immutable'
        ]
    }).inserted_id
    
    challenge_3_5 = challenges_collection.insert_one({
        'title': 'Set Operations',
        'description': 'Create two sets: {1, 2, 3} and {3, 4, 5}. Print their union.',
        'xp_reward': 50,
        'difficulty': 'Medium',
        'input_description': 'Sets: {1, 2, 3} and {3, 4, 5}',
        'output': '{1, 2, 3, 4, 5}',
        'hints': [
            'Use .union() or | operator',
            'Sets automatically remove duplicates',
            'Convert to sorted list for consistent output'
        ]
    }).inserted_id
    
    # Create Module 3
    modules_collection.insert_one({
        'name': 'Data Structures',
        'description': 'Learn about Python data structures: lists, tuples, dictionaries, and sets',
        'challenges': [challenge_3_1, challenge_3_2, challenge_3_3, challenge_3_4, challenge_3_5],
        'order': 3
    })
    print("✓ Module 3 added with 5 challenges")
    
    
    # Module 4: Loops and Iteration
    print("\nAdding Module 4: Loops and Iteration...")
    
    challenge_4_1 = challenges_collection.insert_one({
        'title': 'For Loop Basics',
        'description': 'Use a for loop to print numbers from 1 to 5, each on a new line.',
        'xp_reward': 50,
        'difficulty': 'Easy',
        'input_description': 'Print 1 to 5',
        'output': '1\n2\n3\n4\n5',
        'hints': [
            'Use range(1, 6)',
            'Use print() inside the loop',
            'Each number on a new line'
        ]
    }).inserted_id
    
    challenge_4_2 = challenges_collection.insert_one({
        'title': 'Sum with Loop',
        'description': 'Calculate the sum of numbers from 1 to 10 using a loop and print the result.',
        'xp_reward': 50,
        'difficulty': 'Easy',
        'input_description': 'Sum from 1 to 10',
        'output': '55',
        'hints': [
            'Initialize a variable to 0',
            'Use a for loop with range(1, 11)',
            'Add each number to the variable'
        ]
    }).inserted_id
    
    challenge_4_3 = challenges_collection.insert_one({
        'title': 'While Loop',
        'description': 'Use a while loop to print even numbers from 2 to 10.',
        'xp_reward': 50,
        'difficulty': 'Medium',
        'input_description': 'Print even numbers 2-10',
        'output': '2\n4\n6\n8\n10',
        'hints': [
            'Start with i = 2',
            'Continue while i <= 10',
            'Increment by 2'
        ]
    }).inserted_id
    
    challenge_4_4 = challenges_collection.insert_one({
        'title': 'List Iteration',
        'description': 'Iterate through the list ["apple", "banana", "cherry"] and print each item.',
        'xp_reward': 50,
        'difficulty': 'Easy',
        'input_description': 'List: ["apple", "banana", "cherry"]',
        'output': 'apple\nbanana\ncherry',
        'hints': [
            'Use for item in list',
            'Print each item',
            'Each on a new line'
        ]
    }).inserted_id
    
    challenge_4_5 = challenges_collection.insert_one({
        'title': 'Nested Loops',
        'description': 'Use nested loops to print a 3x3 pattern of stars (*). Each row on a new line.',
        'xp_reward': 50,
        'difficulty': 'Medium',
        'input_description': 'Print 3x3 star pattern',
        'output': '***\n***\n***',
        'hints': [
            'Outer loop for rows',
            'Inner loop for columns',
            'Use print() without newline inside inner loop'
        ]
    }).inserted_id
    
    modules_collection.insert_one({
        'name': 'Loops and Iteration',
        'description': 'Master loops: for loops, while loops, and iteration techniques',
        'challenges': [challenge_4_1, challenge_4_2, challenge_4_3, challenge_4_4, challenge_4_5],
        'order': 4
    })
    print("✓ Module 4 added with 5 challenges")
    
    
    # Module 5: Functions
    print("\nAdding Module 5: Functions...")
    
    challenge_5_1 = challenges_collection.insert_one({
        'title': 'Define a Function',
        'description': 'Create a function called "greet" that prints "Hello, World!" and call it.',
        'xp_reward': 50,
        'difficulty': 'Easy',
        'input_description': 'Function that prints greeting',
        'output': 'Hello, World!',
        'hints': [
            'Use def keyword',
            'Function name: greet',
            'Call the function after defining'
        ]
    }).inserted_id
    
    challenge_5_2 = challenges_collection.insert_one({
        'title': 'Function with Parameters',
        'description': 'Create a function "add_numbers(a, b)" that returns the sum. Call it with 5 and 3, and print the result.',
        'xp_reward': 50,
        'difficulty': 'Easy',
        'input_description': 'Add 5 and 3',
        'output': '8',
        'hints': [
            'Use return statement',
            'Pass two parameters',
            'Print the returned value'
        ]
    }).inserted_id
    
    challenge_5_3 = challenges_collection.insert_one({
        'title': 'Function with Default Parameters',
        'description': 'Create a function "power(base, exp=2)" that calculates base^exp. Call it with 3 (should use default exp=2) and print result.',
        'xp_reward': 50,
        'difficulty': 'Medium',
        'input_description': 'Calculate 3^2',
        'output': '9',
        'hints': [
            'Use ** operator for power',
            'Set default exp=2',
            'Call with only one argument'
        ]
    }).inserted_id
    
    challenge_5_4 = challenges_collection.insert_one({
        'title': 'Return Multiple Values',
        'description': 'Create a function that returns both sum and product of two numbers (4 and 5). Print both results separated by a space.',
        'xp_reward': 50,
        'difficulty': 'Medium',
        'input_description': 'Sum and product of 4 and 5',
        'output': '9 20',
        'hints': [
            'Return a tuple',
            'Unpack the tuple',
            'Print with space separator'
        ]
    }).inserted_id
    
    challenge_5_5 = challenges_collection.insert_one({
        'title': 'Recursive Function',
        'description': 'Create a recursive function to calculate factorial of 5 and print the result.',
        'xp_reward': 50,
        'difficulty': 'Hard',
        'input_description': 'Factorial of 5',
        'output': '120',
        'hints': [
            'Base case: if n <= 1, return 1',
            'Recursive case: n * factorial(n-1)',
            'Call with 5'
        ]
    }).inserted_id
    
    modules_collection.insert_one({
        'name': 'Functions',
        'description': 'Learn to create and use functions, parameters, return values, and recursion',
        'challenges': [challenge_5_1, challenge_5_2, challenge_5_3, challenge_5_4, challenge_5_5],
        'order': 5
    })
    print("✓ Module 5 added with 5 challenges")
    
    
    # Module 6: String Manipulation
    print("\nAdding Module 6: String Manipulation...")
    
    challenge_6_1 = challenges_collection.insert_one({
        'title': 'String Concatenation',
        'description': 'Concatenate "Hello" and "Python" with a space between them and print the result.',
        'xp_reward': 50,
        'difficulty': 'Easy',
        'input_description': 'Combine two strings',
        'output': 'Hello Python',
        'hints': [
            'Use + operator',
            'Add a space " " between',
            'Or use string formatting'
        ]
    }).inserted_id
    
    challenge_6_2 = challenges_collection.insert_one({
        'title': 'String Methods',
        'description': 'Take the string "python programming" and print it in uppercase.',
        'xp_reward': 50,
        'difficulty': 'Easy',
        'input_description': 'Convert to uppercase',
        'output': 'PYTHON PROGRAMMING',
        'hints': [
            'Use .upper() method',
            'Methods don\'t modify original',
            'Print the result'
        ]
    }).inserted_id
    
    challenge_6_3 = challenges_collection.insert_one({
        'title': 'String Slicing',
        'description': 'From the string "Python3.11", extract and print only "Python".',
        'xp_reward': 50,
        'difficulty': 'Medium',
        'input_description': 'Extract "Python" from "Python3.11"',
        'output': 'Python',
        'hints': [
            'Use string slicing [start:end]',
            'Python is first 6 characters',
            'Use [:6]'
        ]
    }).inserted_id
    
    challenge_6_4 = challenges_collection.insert_one({
        'title': 'String Replace',
        'description': 'Replace "Java" with "Python" in the string "I love Java" and print it.',
        'xp_reward': 50,
        'difficulty': 'Easy',
        'input_description': 'Replace Java with Python',
        'output': 'I love Python',
        'hints': [
            'Use .replace() method',
            'Syntax: str.replace(old, new)',
            'Print the result'
        ]
    }).inserted_id
    
    challenge_6_5 = challenges_collection.insert_one({
        'title': 'Split and Join',
        'description': 'Split "apple,banana,cherry" by comma, then join with "-" and print.',
        'xp_reward': 50,
        'difficulty': 'Medium',
        'input_description': 'Split by comma, join with dash',
        'output': 'apple-banana-cherry',
        'hints': [
            'Use .split(",")',
            'Use "-".join(list)',
            'Chain the operations'
        ]
    }).inserted_id
    
    modules_collection.insert_one({
        'name': 'String Manipulation',
        'description': 'Master string operations: concatenation, methods, slicing, and formatting',
        'challenges': [challenge_6_1, challenge_6_2, challenge_6_3, challenge_6_4, challenge_6_5],
        'order': 6
    })
    print("✓ Module 6 added with 5 challenges")
    
    print("\n✅ All modules added successfully!")
    print("Total new modules: 4")
    print("Total new challenges: 20")

if __name__ == '__main__':
    print("=" * 60)
    print("CodeXcel - Adding More Modules")
    print("=" * 60)
    add_modules_and_challenges()
    print("=" * 60)
    print("\nYou can now restart your Flask app and see the new modules!")
