# dog-training-reservations

## Run dev server
1. Create virtual environment: `python -m venv django-env`
2. Activate virtual environment: `source django-env/bin/activate `
3. Install packages: `pip install -r requirements.txt`
4. Run dev server: `python manage.py runserver`

## Create database
1. Run all migrations: `python manage.py migrate`

## Changes in model
1. Prepare migration files: `python manage.py makemigrations`
2. Run migration file: `python manage.py migrate`

## Create admin user
Can be done by command: `python manage.py createsuperuser`
[Complete how to tutorial on this link](https://docs.djangoproject.com/en/4.1/intro/tutorial02/#creating-an-admin-user)
