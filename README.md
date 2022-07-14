# django-project-template
Setup - only once
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create project - only once

```bash
django-admin startproject test_project
cd test_project
django-admin startapp test_app
```

Run the project
```bash
python manage.py migrate
python manage.py runserver
```