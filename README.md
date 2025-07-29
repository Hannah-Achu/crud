# 📚 Django Student CRUD App

A simple Django web application built during my internship to manage student data using basic CRUD operations (Create, Read, Update, Delete).

## 🚀 Features
- 🧾 Add new student (Name, Email, Password)
- 🛠 Edit existing student details
- ❌ Delete a student
- 📄 View student table with data
- ✅ Uses Django's built-in SQLite database

## 🛠 Tech Stack
- Django (Python Framework)
- SQLite (Default DB)
- HTML & CSS
- Bootstrap (for styling)



## ⚙️ How to Run This Project

```bash
# Clone the repository
git clone https://github.com/Hannah-Achu/django-student-crud-app.git

# Navigate into the project folder
cd django-student-crud-app

# Create and activate virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate      # On Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
