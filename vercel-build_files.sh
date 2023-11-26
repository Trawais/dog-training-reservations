python3.9 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

echo "Python venv path: ${VIRTUAL_ENV}"

echo "Postgres database: ${POSTGRES_DATABASE}"
echo "Postgres user: ${POSTGRES_USER}"
echo "Postgres password: ${POSTGRES_PASSWORD}"
echo "Postgres host: ${POSTGRES_HOST}"
echo "Postgres port: ${POSTGRES_PORT}"

pip install -r requirements.txt

python3.9 manage.py migrate
python3.9 manage.py collectstatic

# env var DJANGO_SUPERUSER_PASSWORD must be set
# env var DJANGO_SUPERUSER_EMAIL must be set
# env var DJANGO_SUPERUSER_USERNAME must be set
./manage.py createsuperuser --no-input || true
