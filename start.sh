#!/usr/bin/env bash
set -e

echo "==> [Startup] Preparing environment..."

# Persistent storage check (if /var/data or $DATA_DIR exists)
PERSISTENT_DIR="${DATA_DIR:-/var/data}"
if [ -d "$PERSISTENT_DIR" ]; then
    echo "==> [Storage] Initializing persistent directory at $PERSISTENT_DIR..."
    mkdir -p "$PERSISTENT_DIR/media"
    if [ ! -f "$PERSISTENT_DIR/db.sqlite3" ] && [ -f "db.sqlite3" ]; then
        cp db.sqlite3 "$PERSISTENT_DIR/db.sqlite3"
    fi
    if [ -d "media" ]; then
        cp -rn media/* "$PERSISTENT_DIR/media/" 2>/dev/null || true
    fi
fi

# Run migrations
echo "==> [Database] Applying migrations..."
python manage.py migrate --noinput

# Seed data and superuser (kishanraja / kishanraja12345)
echo "==> [Database] Verifying seed data and admin account..."
python manage.py seed_data

# Collect static files
echo "==> [Static Files] Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn server
PORT="${PORT:-8000}"
echo "==> [Server] Starting Gunicorn on 0.0.0.0:$PORT..."
exec gunicorn config.wsgi:application --bind "0.0.0.0:$PORT" --workers 2 --threads 4 --timeout 120
