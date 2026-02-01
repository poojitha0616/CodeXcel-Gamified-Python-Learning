# CodeXcel-Gamified-Python-Learning
Gamified Python learning platform built using HCI principles

# CodeXcel - Gamified Python Learning Environment

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-5.0+-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A complete Flask web application that gamifies Python learning with XP, levels, badges, and real-time code execution powered by Judge0 API.

## 🌟 Features

- **Gamification System**: Earn XP, level up, and unlock badges
- **Real-Time Code Execution**: Judge0 API integration for Python code evaluation
- **User Authentication**: Secure session-based login with password hashing
- **Learning Modules**: Organized Python topics (Variables, Loops, Functions, etc.)
- **Leaderboard**: Compete with other learners
- **Admin Panel**: Manage challenges and view users
- **Beautiful UI**: Bootstrap 5 with custom styling and animations

## 🎮 Gamification Logic

- **XP System**: +50 XP for each correct submission
- **Level Calculation**: Level = XP // 500 + 1
- **Badges**: Unlock achievements for milestones
  - "First Challenge" - Complete your first challenge
  - "Problem Solver" - Complete 5 challenges
  - "Level 5 Master" - Reach Level 5

## 🏗️ Project Structure

```
CodeXcel/
├── app.py                          # Main Flask application
├── config.py                       # Configuration settings
├── requirements.txt                # Python dependencies
├── seed_data.py                   # Database seeding script
├── README.md                      # Documentation
├── static/
│   └── css/
│       └── style.css              # Custom styles
└── templates/
    ├── base.html                  # Base template
    ├── index.html                 # Landing page
    ├── login.html                 # Login page
    ├── register.html              # Registration page
    ├── dashboard.html             # User dashboard
    ├── modules.html               # Learning modules list
    ├── challenge.html             # Challenge page with code editor
    ├── leaderboard.html           # Leaderboard
    ├── profile.html               # User profile
    ├── admin.html                 # Admin panel
    ├── admin_add_challenge.html   # Add challenge form
    └── admin_edit_challenge.html  # Edit challenge form
```

## 🗄️ MongoDB Collections

### users
```json
{
  "_id": ObjectId,
  "username": String,
  "email": String,
  "password_hash": String,
  "xp": Number,
  "level": Number,
  "badges": Array,
  "role": String  // "user" or "admin"
}
```

### modules
```json
{
  "_id": ObjectId,
  "name": String,
  "description": String,
  "challenges": Array  // Array of challenge IDs
}
```

### challenges
```json
{
  "_id": ObjectId,
  "title": String,
  "description": String,
  "input": String,
  "output": String,
  "xp_reward": Number,
  "module_id": ObjectId
}
```

### submissions
```json
{
  "_id": ObjectId,
  "user_id": ObjectId,
  "challenge_id": ObjectId,
  "code": String,
  "result": String,  // "success" or "failed"
  "timestamp": Number
}
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.9 or higher
- MongoDB 5.0 or higher
- Judge0 RapidAPI Key (for code execution)

### Step 1: Clone or Download

```bash
cd CodeXcel
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Start MongoDB

Make sure MongoDB is running on your system:

**Windows:**
```bash
# Start MongoDB service
net start MongoDB
```

**Mac/Linux:**
```bash
# Start MongoDB
mongod --config /usr/local/etc/mongod.conf
```

Or use MongoDB Atlas (cloud) and update the `MONGO_URI` in `config.py`.

### Step 4: Configure Judge0 API (Optional but Recommended)

1. Get a free API key from [RapidAPI Judge0](https://rapidapi.com/judge0-official/api/judge0-ce)
2. Update `config.py`:

```python
JUDGE0_API_KEY = 'your-rapidapi-key-here'
```

**Note:** The app will work without Judge0 API, but code execution will return errors. You can test other features without it.

### Step 5: Seed the Database

```bash
python seed_data.py
```

This creates:
- Admin user (username: `admin`, password: `admin123`)
- 2 test users
- 2 modules (Python Basics, Control Flow & Loops)
- 5 sample challenges

### Step 6: Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## 🎯 Usage

### For Students

1. **Register** a new account or **Login**
2. Browse **Modules** to see available Python topics
3. Select a **Challenge** and write your Python code
4. **Run Code** to test or **Submit Solution** to earn XP
5. Check **Dashboard** to see your progress, level, and badges
6. View **Leaderboard** to see how you rank against others
7. Visit **Profile** to edit your information and view completed challenges

### For Admins

1. Login with admin credentials
2. Access **Admin Panel** from the dropdown menu
3. **Add New Challenges** with title, description, expected output, and XP reward
4. **Edit or Delete** existing challenges
5. View all users and their statistics

## 📚 Available Routes

### Public Routes
- `/` - Landing page
- `/login` - User login
- `/register` - User registration

### Protected Routes (Login Required)
- `/dashboard` - User dashboard with stats
- `/modules` - Learning modules list
- `/challenge/<id>` - Challenge page with code editor
- `/leaderboard` - Global leaderboard
- `/profile` - User profile
- `/logout` - Logout

### Admin Routes (Admin Access Required)
- `/admin` - Admin panel
- `/admin/challenge/add` - Add new challenge
- `/admin/challenge/edit/<id>` - Edit challenge
- `/admin/challenge/delete/<id>` - Delete challenge

## 🔧 Tech Stack

- **Backend**: Flask 2.3.3
- **Database**: MongoDB (PyMongo 4.5.0)
- **Frontend**: HTML5, Bootstrap 5, Jinja2 Templates
- **Authentication**: Flask Sessions with Werkzeug password hashing
- **Code Execution**: Judge0 API (Python 3.8.1)
- **Icons**: Bootstrap Icons

## 🎨 Features Breakdown

### XP & Leveling System
- Earn 50 XP per successful challenge (configurable)
- Level up every 500 XP
- Real-time progress bar showing XP to next level

### Badge System
- Automatic badge awarding for achievements
- Displayed on dashboard and profile
- Visual recognition of accomplishments

### Code Editor
- Syntax highlighting for Python
- Run code to test output
- Submit to validate against expected output
- Real-time feedback with detailed error messages

### Leaderboard
- Sorted by XP (highest to lowest)
- Shows level, badges, and rank
- Highlights current user

### Admin Panel
- Full CRUD operations for challenges
- User management view
- Statistics dashboard

## 🔐 Security Features

- Passwords hashed using Werkzeug's `generate_password_hash()`
- Session-based authentication
- Role-based access control (user/admin)
- Protected routes with decorators

## 🐛 Troubleshooting

### MongoDB Connection Error
```
Error: Connection refused
```
**Solution**: Make sure MongoDB is running on `localhost:27017`

### Judge0 API Errors
```
Error: Failed to create submission
```
**Solution**: 
1. Verify your RapidAPI key in `config.py`
2. Check your RapidAPI subscription is active
3. Ensure you have available requests in your quota

### Port Already in Use
```
Error: Address already in use
```
**Solution**: Change the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Use a different port
```

## 📝 Sample Test Data

After running `seed_data.py`, you can login with:

**Admin Account:**
- Username: `admin`
- Password: `admin123`

**Test User Account:**
- Username: `john_doe`
- Password: `password123`

## 🔮 Future Enhancements

- [ ] Add more programming languages
- [ ] Implement achievements system
- [ ] Add social features (comments, discussions)
- [ ] Create difficulty levels for challenges
- [ ] Add hints system
- [ ] Implement challenge ratings
- [ ] Add code sharing functionality
- [ ] Create mobile-responsive improvements
- [ ] Add user avatars
- [ ] Implement email notifications

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Created with ❤️ for Python learners everywhere!

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📞 Support

If you need help or have questions:
1. Check the troubleshooting section
2. Review the code comments
3. Ensure all dependencies are installed

---

**Happy Coding! 🚀🐍**

