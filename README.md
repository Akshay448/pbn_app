# PNB starter project   
Setup - This django project is running in a venv, setup by python 3.7

## Running th project
Running the project might not work but can be tried
1. Clone th project
2. Make sure postgres is running in local system 
3. With postgres running, follow these commands in a terminal [database setup](#database-setup)
4. Run migrations - follow these steps - [managing migrations with alembic](#managing-database-migrations-with-alembic)
5. Go to localhost:8000/list  to see all the patients, start adding a nw patient from the browser

## Info
Viewsets are not created here because they were creating problems when using sqlalchemy base model
otherwise if not using sqlalchemy base model and instead using viewset.ModelViewSt, i created a simple viewset with below code
```bashh
# DRF ViewSet for API interactions
# class PatientViewSet(viewsets.ModelViewSet):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer
```
and setting the url as this
```bash
    url('api/', include(router.urls)),  # API endpoints with viewset
```

With this setup, it was simple to get api endpoints which can be exposed with an api gateway
but skipping it for now to have sqlalchemy base model serve the frontend views

# Table of contents
1. [Starting the Django project](#starting-the-django-project)
2. [Creating applications](#creating-apps-for-patients-and-sqlalchemy-engine)
3. [Database setup](#database-setup)
4. [Managing migrations with alembic](#managing-database-migrations-with-alembic)

## Starting the Django project
```bash
django-admin startproject pbn1
```

## Creating apps for patients and sqlalchemy engine
```bash
python manage.py startapp patients
python manage.py startapp sqlalchemy_integration
```


## Database setup
```bash
psql

CREATE ROLE practice_rw WITH LOGIN PASSWORD 'your_password' CREATEDB;

CREATE DATABASE practice_data OWNER practice_rw;

GRANT ALL PRIVILEGES ON DATABASE practice_data TO practice_rw;

\q
```

## Managing Database Migrations with Alembic
```bash
alembic revision --autogenerate -m "Your message here"

alembic upgrade head
```

