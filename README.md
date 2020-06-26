# Flask architecture using Blueprint

It uses Flask-RESTPlus(Swagger-UI), Flask-Admin, JWT authentication, SQL Alchemy and Celery.

---

## Clone

```bash
$git clone https://github.com/wilson-boca/flask-boilerplate-blueprint.git
```

## Environment

Python 3.6+
Activate your virtualenv (mkvirtualenv, venv, etc)

## Install requirements

```bash
$pip install -r requirements.txt
$pip install -r requirements_dev.txt
$pip install -r requirements_test.txt
```

## Setting up database

```
$ sudo apt install postgress
$ sudo su postgres
$ psql
$ CREATE ROLE admin SUPERUSER LOGIN PASSWORD 'admin321';
$ CREATE DATABASE apidb;
$ ALTER DATABASE apidb OWNER TO admin;
$ \q
$ exit
```
## Testing

```bash
$pytest flaskapp/tests

It's under construction...
```

## Running

```bash
$flask create-db
$flask populate-db
$flask add-user -u admin -p 123456
$flask run

Added users from terminal are all admins
```

## Starting Celery Workers

```bash
Main queue for quick tasks (Like sendmail)
$celery worker -A flaskapp.celery_ext.celery_worker.celery --loglevel=info --pool=solo

Slow queue for slow(heavy) tasks
$worker -A flaskapp.celery_ext.celery_worker.celery --loglevel=info --queue slow
```

## Calling the API:

- Website: http://localhost:5000
- Admin: http://localhost:5000/admin/
- Swagger-UI: http://localhost:5000/api/v1 
- API calls:
  - http://127.0.0.1:5000/api/v1/users - Add user (POST)
  - http://127.0.0.1:5000/api/v1/users - Users list (GET)
  - http://127.0.0.1:5000/api/v1/users/1 - User with id 1 (GET)
  - http://127.0.0.1:5000/api/v1/login - Logout user (POST)
  - http://127.0.0.1:5000/api/v1/logout - Logout user (POST)
  - http://127.0.0.1:5000/api/v1/celery/coffee/your_name - Make a celery quick coffee for you (GET)
  - http://127.0.0.1:5000/api/v1/celery/capuccino/your_name - Make a celery slow capuccino for you (GET)
