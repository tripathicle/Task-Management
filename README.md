# Task Manager

![Django](https://img.shields.io/badge/Django-4.2-092E20?style=flat-square&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)

A **simple yet robust** To-Do application built with **Django**, designed for task management with a focus on clean code and easy setup.
<img width="218" alt="image" src="https://github.com/tripathicle/Task-Management/blob/main/Task_manager.png" />


---

## 📖 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🌟 Overview
The Django To-Do App is a lightweight task management application that allows users to create, update, and delete tasks. It includes a basic admin interface for managing tasks and users, making it a great starting point for learning Django or building a small-scale application.


## ✨ Features
- 📋 Create, update, and delete tasks
- 🔒 Admin panel for user and task management
- 🗄️ SQLite database for local development
- 🛠️ Modular Django app structure

---

## 🛠️ Prerequisites
Before starting, ensure you have:
- **Python 3.8+** installed
- **Git** for version control
- A code editor (e.g., VS Code)

---

## 🚀 Setup Instructions

Follow these steps to set up the project locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/sktripathiinfo/django_todo_app.git
   cd django_todo_app
   ```

2. **Set Up Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   Ensure you have a `requirements.txt` file. If not, create one with at least Django:
   ```bash
   echo "Django>=4.2" > requirements.txt
   pip install -r requirements.txt
   ```

4. **Run Database Migrations**
   The project uses SQLite by default (`db.sqlite3` is created automatically):
   ```bash
   python manage.py migrate
   ```

5. **Create Admin User**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start Development Server**
   ```bash
   python manage.py runserver
   ```
   - App: `http://localhost:8000`
   - Admin Panel: `http://localhost:8000/admin`

---

## 📂 Project Structure
Below is the complete folder structure of the Django To-Do App:

```
django_todo_app/
├── todo_app/               # Main application
│   ├── migrations/         # Database migrations
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── 0002_auto_202505.py
│   ├── templates/          # HTML templates (if any)
│   ├── __init__.py
│   ├── admin.py            # Admin interface config
│   ├── apps.py             # App configuration
│   ├── models.py           # Database models
│   ├── tests.py            # Unit tests
│   ├── urls.py             # App-specific URLs
│   └── views.py            # Application logic
├── todo_project/           # Django project settings
│   ├── __init__.py
│   ├── settings.py         # Project settings
│   ├── urls.py             # Project URLs
│   └── wsgi.py             # WSGI entry point
├── venv/                   # Virtual environment
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

### Key Files and Folders
- **`todo_app/`**: Contains the core application logic, including models, views, and URLs.
- **`todo_project/`**: Holds the project-level settings and configurations.
- **`migrations/`**: Stores database migration files, such as `0001_initial.py` for initial setup and `0002_auto_202505.py` for later changes.
- **`venv/`**: Virtual environment folder (not tracked in Git).
- **`db.sqlite3`**: Default SQLite database for local development.

---

## 🚨 Troubleshooting

### Common Issues
1. **Database Migration Errors**
   If migrations fail:
   ```bash
   python manage.py migrate --run-syncdb
   ```

2. **Missing Dependencies**
   Ensure all dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

3. **Port Conflicts**
   If port 8000 is in use:
   ```bash
   # Find process using port 8000
   sudo lsof -i :8000
   # Kill process
   kill -9 <PID>
   ```

For additional issues, check the terminal output or Django logs.

---

## 🤝 Contributing
Contributions are welcome! Follow these steps:
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/AmazingFeature`
3. Commit changes: `git commit -m 'Add AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

---

## 📜 License
This project is licensed under the MIT License. See `LICENSE` for details.

---

**Built with ❤️ by Tripathicle**  
For support, open an issue on GitHub.
