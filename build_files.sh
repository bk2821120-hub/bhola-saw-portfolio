#!/usr/bin/env bash
echo "==> [Vercel Build] Installing dependencies..."
python3 -m pip install -r requirements.txt

echo "==> [Vercel Build] Collecting static files..."
python3 manage.py collectstatic --noinput --clear

echo "==> [Vercel Build] Finished successfully."
