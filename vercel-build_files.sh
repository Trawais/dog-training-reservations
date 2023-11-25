python3.9 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

echo $VIRTUAL_ENV

echo $POSTGRES_DATABASE
echo $POSTGRES_USER
echo $POSTGRES_PASSWORD
echo $POSTGRES_HOST
echo $POSTGRES_PORT

pip install -r requirements.txt

python3.9 manage.py migrate
python3.9 manage.py collectstatic

# env var DJANGO_SUPERUSER_PASSWORD must be set
# env var DJANGO_SUPERUSER_EMAIL must be set
# env var DJANGO_SUPERUSER_USERNAME must be set
./manage.py createsuperuser --no-input || true
