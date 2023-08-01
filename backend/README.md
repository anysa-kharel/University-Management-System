# GETTING START
## install the following in your computer
```bash
pip install django
pip install djangorestframework
pipenv install djangorestframework django-cors-headers
```

## To run server
### linux
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
### If you want to create admin login then create superuser by
```bash
python3 manage.py createsuperuser
```

## NOTE: IF python3 is not working try replacing python3 by python in every command