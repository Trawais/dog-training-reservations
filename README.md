# dog-training-reservations

## Run dev server
1. Create virtual environment: `python -m venv .venv`
2. Activate virtual environment: `source .env/bin/activate `
3. Install packages: `pip install -r requirements.txt`
4. Run dev server: `DEBUG=True python manage.py runserver`

### Debug mode
In `dog_school/settings.py` file you can see the debug mode is led by `DEBUG` env var.
If it is set to `True` (yes, with capital `T`) the debug mode is active.
Otherwise the production mode (non-debug) is used.

## Create database
1. Run all migrations: `python manage.py migrate`

## Changes in model
1. Prepare migration files: `python manage.py makemigrations`
2. Run migration file: `python manage.py migrate`

## Create admin user
Can be done by command: `python manage.py createsuperuser`
[Complete how to tutorial on this link](https://docs.djangoproject.com/en/4.1/intro/tutorial02/#creating-an-admin-user)
