#!/usr/bin/env bash
set -e

echo "==> [Render Start] Preparing application runtime environment..."

# 1. Render Persistent Storage Setup (if /var/data or $DATA_DIR exists)
PERSISTENT_DIR="${DATA_DIR:-/var/data}"

if [ -d "$PERSISTENT_DIR" ]; then
    echo "==> [Render Storage] Persistent storage directory found at $PERSISTENT_DIR"
    mkdir -p "$PERSISTENT_DIR/media"

    # If persistent SQLite database doesn't exist yet, copy initial repo database if available
    if [ ! -f "$PERSISTENT_DIR/db.sqlite3" ] && [ -f "db.sqlite3" ]; then
        echo "==> [Render Storage] Initializing persistent database from repo db.sqlite3..."
        cp db.sqlite3 "$PERSISTENT_DIR/db.sqlite3"
    fi

    # Sync existing media files to persistent storage if not already copied
    if [ -d "media" ]; then
        echo "==> [Render Storage] Syncing bundled media files to persistent storage..."
        cp -rn media/* "$PERSISTENT_DIR/media/" 2>/dev/null || true
    fi
else
    echo "==> [Render Storage] Standard storage mode."
fi

# 2. Database Migrations
echo "==> [Database] Applying migrations..."
python manage.py migrate --noinput

# 3. Seed initial data and verify admin superuser
echo "==> [Database] Verifying seed data and admin account..."
python manage.py seed_data

# 4. Collect static files
echo "==> [Static Files] Collecting static files..."
python manage.py collectstatic --noinput

# 5. Start Gunicorn
PORT="${PORT:-8000}"
echo "==> [Gunicorn] Starting application server on 0.0.0.0:$PORT..."
exec gunicorn config.wsgi:application --bind "0.0.0.0:$PORT" --workers 2 --threads 4 --timeout 120
