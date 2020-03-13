# Flask architecture using Blueprint

Based on [https://codeshow.com.br/arquitetura-web-python-flask/](https://codeshow.com.br/arquitetura-web-python-flask/) from Bruno Rocha.
Watch his video on YouTube channel, it's amazing.

It uses Flask-RESTPlus(Swagger-UI), Flask-Admin and JWT authentication.

---

## Clone

```bash
git clone https://github.com/wilson-boca/flask-boilerplate-blueprint.git
```

## Environment

Python 3.6+
Activate your virtualenv (mkvirtualenv)

## Install requirements

```bash
pip install -r requirements.txt
pip install -r requirements_dev.txt
pip install -r requirements_test.txt
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
pytest flaskapp/tests
```

## Running

```bash
flask create-db
flask populate-db
flask add-user -u admin -p 123456
flask run

Users inserted from command line are admins
```

## Calling the API:

- Website: http://localhost:5000
- Admin: http://localhost:5000/admin/
- Swagger-UI: http://localhost:5000/api/v1 
- API:
  - http://127.0.0.1:5000/api/v1/users - Add user (POST)
  - http://127.0.0.1:5000/api/v1/users - Users list (GET)
  - http://127.0.0.1:5000/api/v1/users/1 - User with id 1 (GET)
  - http://127.0.0.1:5000/api/v1/login - Logout user (POST)
  - http://127.0.0.1:5000/api/v1/logout - Logout user (POST)
 