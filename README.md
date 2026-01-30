

# 📘 Django Course Management API

A Django REST Framework–based backend for managing **users, courses, modules, and enrollments**.  
This project supports role-based users (e.g. instructor, student) and exposes APIs for course creation and enrollment.

---

## 🚀 Features

- Custom User model  
- Role-based users (Student / Instructor)  
- Course & Module management  
- Student enrollments  
- Django REST Framework serializers  
- Clean project structure  
- Ready for JWT / API authentication  

---

## 🛠 Tech Stack

- **Python 3.11**
- **Django**
- **Django REST Framework**
- **SQLite** (default, easy to switch)
- **Git & GitHub**

---

## 📁 Project Structure


course/
│
├── core/                 # Django project settings
│   ├── core/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── manage.py
│
├── learning/             # Main application
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── db.sqlite3
├── requirements.txt
└── README.md



⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/your-username/django-course-api.git
cd django-course-api

2️⃣ Create virtual environment
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Mac / Linux

source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt


If requirements.txt doesn’t exist yet:

pip install django djangorestframework

4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create superuser
python manage.py createsuperuser

6️⃣ Run development server
python manage.py runserver


Visit:

Admin panel → http://127.0.0.1:8000/admin/

API base → http://127.0.0.1:8000/

🔐 Custom User Model

This project uses a custom User model defined in the learning app.

AUTH_USER_MODEL = 'learning.User'


⚠️ Must be defined before running migrations.

📦 API Modules

Users

Courses

Modules

Enrollments

Serializers are defined in:

learning/serializers.py

🧪 Development Notes

Default database: SQLite

DEFAULT_AUTO_FIELD set to BigAutoField

Virtual environment excluded via .gitignore

📌 Future Improvements

JWT Authentication

Permissions & role-based access

Course progress tracking

API documentation (Swagger / Redoc)

Docker support

👤 Author

Jatin Shrivastav
Learning Django & Django REST Framework 🚀

⭐️ Support

If you find this project helpful, feel free to ⭐ star the repository!
