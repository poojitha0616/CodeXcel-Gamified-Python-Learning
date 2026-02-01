"""
Seed script to populate MongoDB with initial data
Run this after setting up MongoDB: python seed_data.py
"""

from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from bson.objectid import ObjectId
import os

# MongoDB connection - use environment variable or localhost
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/codexcel')
# MONGO_URI = "mongodb+srv://ksanithkumar2003_db_user:6VMYxXGFZ2wB0kVW@cluster0.ss38xix.mongodb.net/?appName=Cluster0"
print(f"Connecting to MongoDB...")
client = MongoClient(MONGO_URI)
db = client.codexcel

# Clear existing data
print("Clearing existing data...")
db.users.delete_many({})
db.modules.delete_many({})
db.challenges.delete_many({})
db.submissions.delete_many({})

# Create admin user
print("\nCreating admin user...")
admin_user = {
    'username': 'admin',
    'email': 'admin@codexcel.com',
    'password_hash': generate_password_hash('admin123'),
    'xp': 1000,
    'level': 3,
    'badges': ['Early Adopter', 'Admin Badge'],
    'role': 'admin',
    'unlocked_themes': ['default', 'dark-neon'],
    'avatar_styles': ['default', 'robot'],
    'active_theme': 'default',
    'active_avatar': 'default'
}
admin_id = db.users.insert_one(admin_user).inserted_id
print(f"✓ Admin user created (username: admin, password: admin123)")

# Create test users
print("\nCreating test users...")
test_users = [
    {
        'username': 'john_doe',
        'email': 'john@example.com',
        'password_hash': generate_password_hash('password123'),
        'xp': 750,
        'level': 2,
        'badges': ['First Challenge', 'Problem Solver'],
        'role': 'user',
        'unlocked_themes': ['default'],
        'avatar_styles': ['default'],
        'active_theme': 'default',
        'active_avatar': 'default'
    },
    {
        'username': 'jane_smith',
        'email': 'jane@example.com',
        'password_hash': generate_password_hash('password123'),
        'xp': 500,
        'level': 2,
        'badges': ['First Challenge'],
        'role': 'user',
        'unlocked_themes': ['default'],
        'avatar_styles': ['default'],
        'active_theme': 'default',
        'active_avatar': 'default'
    }
]

for user in test_users:
    db.users.insert_one(user)
    print(f"✓ User created: {user['username']}")

# Create modules
print("\nCreating modules...")
modules_data = [
    {
        'name': 'Python Basics',
        'description': 'Learn fundamental Python concepts including variables, data types, and basic operations.',
        'challenges': []
    },
    {
        'name': 'Control Flow & Loops',
        'description': 'Master conditional statements, loops, and program flow control in Python.',
        'challenges': []
    }
]

module_ids = []
for module_data in modules_data:
    module_id = db.modules.insert_one(module_data).inserted_id
    module_ids.append(module_id)
    print(f"✓ Module created: {module_data['name']}")

# Create challenges
print("\nCreating challenges...")
challenges_data = [
    {
        'title': 'Hello World',
        'description': 'Write a program that prints "Hello, World!" to the console.',
        'input': 'None',
        'output': 'Hello, World!',
        'xp_reward': 50,
        'module_id': module_ids[0]
    },
    {
        'title': 'Simple Addition',
        'description': 'Write a program that prints the sum of 5 and 3.',
        'input': 'None',
        'output': '8',
        'xp_reward': 50,
        'module_id': module_ids[0]
    },
    {
        'title': 'Print Your Name',
        'description': 'Write a program that prints your name.',
        'input': 'None',
        'output': 'Your Name',
        'xp_reward': 50,
        'module_id': module_ids[0]
    },
    {
        'title': 'Even or Odd',
        'description': 'Write a program that checks if the number 10 is even or odd and prints "Even".',
        'input': 'number = 10',
        'output': 'Even',
        'xp_reward': 75,
        'module_id': module_ids[1]
    },
    {
        'title': 'Count to Five',
        'description': 'Write a program that prints numbers from 1 to 5, each on a new line.',
        'input': 'None',
        'output': '1\n2\n3\n4\n5',
        'xp_reward': 75,
        'module_id': module_ids[1]
    }
]

challenge_ids = {}
for idx, challenge_data in enumerate(challenges_data):
    challenge_id = db.challenges.insert_one(challenge_data).inserted_id
    challenge_ids[idx] = str(challenge_id)
    
    # Add challenge to module
    db.modules.update_one(
        {'_id': challenge_data['module_id']},
        {'$push': {'challenges': str(challenge_id)}}
    )
    print(f"✓ Challenge created: {challenge_data['title']}")

print("\n" + "="*50)
print("Database seeded successfully! 🎉")
print("="*50)
print("\nYou can now:")
print("1. Start the Flask app: python app.py")
print("2. Login as admin: username=admin, password=admin123")
print("3. Or login as test user: username=john_doe, password=password123")
print("\nMongoDB is running on: mongodb://localhost:27017/codexcel")
print("="*50)
