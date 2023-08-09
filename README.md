# A Book API(Browseable api)
## The API fetches Tittle, Author and ISBN from the database
In order to run and create this app 
## Here are some procedures
    1. use ensure that pipenv is installed
    2. Run pipenv shell to activate the virtual environment
    3. ``pipenv install django djangorestframework`` to install the required dependencies
    4. create the project and the app by running 
        - ``django-admin startproject project_name``
        - ``python manage.py startapp app_name``
    5. sync and create tables in the database by running:
        - python manage.py migrate
        - python manage.py makemigrations app_name
    6. create the super user by running: ``python manage.py createsuperuser`` and follow the instructions
    7. don't forget to add the installed dependicies to the installed_app from your the project settings
    8. run your development server to test it
    9. dont forget to add this to your repo 