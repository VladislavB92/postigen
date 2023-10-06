#!/bin/bash

echo "${POSTGRES_USER}"

postgres_ready() {
python << END
import sys
import psycopg2
try:
    psycopg2.connect(
        dbname="${POSTGRES_DB}",
        user="${POSTGRES_USER}",
        password="${POSTGRES_PASSWORD}",
        host="${POSTGRES_HOST}",
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}
until postgres_ready; do
  >&2 echo "Waiting for PostgreSQL to become available..."
  sleep 1
done
>&2 echo "PostgreSQL is available"
python manage.py makemigrations
python manage.py migrate
if ! python manage.py shell -c "from parcels.models import Parcel; from lockers.models import Locker; print(Parcel.objects.exists() or Locker.objects.exists())"; then
    # Load fixtures only if data doesn't exist
    python manage.py loaddata fixtures/model_name.json
fi

exec "$@"
