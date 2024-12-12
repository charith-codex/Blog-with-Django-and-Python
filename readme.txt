python -m venv env
env\scripts\activate

pip install django
django-admin startproject Blog
python manage.py startapp HOME

python manage.py runserver

pip install django-autoslug
pip install pillow