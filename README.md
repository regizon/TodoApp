DjangoTodoApp

<img src="https://i.ibb.co/b4RwBY3/2025-12-09-194221.png">

Simple app to manage tasks (CRUD) via Django.
Allows user to register, create tasks, mark as done, edit, delete and prioritize them.

Functions:

1. Login/Register.
2. Tasks CRUD.
3. Tasks prioritizing.
4. Sorting.
5. Search through tasks for one exact.
6. Assigning tasks to a specific user.

Technology stack:

Python 3
Django
HTML and CSS (with Bootstrap)
JS (with Bootstrap scripts)
PostgreSQL

How to start project:

1. Clone this repository

git clone https://github.com/regizon/TodoApp
cd TodoApp 

2. Create virtual environment

python -m venv venv

3. Activate venv

#For Windows:

venv\Scripts\activate

#For Linux/Mac:

source venv/bin/activate

4. Install requirements

pip install -r requirements.txt

5. Create .env file as in example from this repo.

6. Apply migrations

python manage.py migrate

7. Start server

python manage.py runserver
