# Taskmaster

A simple Django todo app with Google OAuth login via django-allauth.

## Setup

```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
cp .env.example .env         # then fill in your own secrets
python manage.py migrate
python manage.py runserver
```

## Features

- Create, edit, delete tasks
- Filter by complete / incomplete
- Google sign-in (django-allauth)
- User avatar in task page (Google photo or username initial)
