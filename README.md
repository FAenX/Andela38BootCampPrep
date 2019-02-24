## Welcome to the API

### to run the django app

```cd AndelaDjango```
```pip install -r requirements.txt```

### then 

```python manage.py migrate```
```python manage.py create superuser```
```python manage.py runserver```

### to run the flask app

 ```cd AndelaFlask```
```pip install -r requirements.txt```

### then

```export FLASK_APP='run.py'
export APP_SETTINGS='development'
export SECRET='a long key'#replace this with a random key
export DATABASE_URL='sqlite:////tmp/andelansflask.db'

python manage.py db init
python manage.py db migrate
python manage.py db upgrade 
flask run```
