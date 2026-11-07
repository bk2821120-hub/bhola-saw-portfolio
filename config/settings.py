"""
Django settings for Portfolio CMS.
"""
import environ
from pathlib import Path

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Environment
env = environ.Env(
    DEBUG=(bool, True),
    ALLOWED_HOSTS=(list, ['localhost', '127.0.0.1', 'testserver', '*']),
)
environ.Env.read_env(BASE_DIR / '.env')

SECRET_KEY = env('SECRET_KEY', default='django-insecure-bhola-portfolio-production-secret-key-2026')
DEBUG = env.bool('DEBUG', default=False)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])
if '*' not in ALLOWED_HOSTS and 'testserver' not in ALLOWED_HOSTS:
    ALLOWED_HOSTS += ['testserver', 'localhost', '127.0.0.1']

# CSRF Trusted Origins for Koyeb, Render, Vercel, and custom domains
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default=[
    'https://*.koyeb.app',
    'https://*.onrender.com',
    'https://*.vercel.app',
    'http://localhost',
    'http://127.0.0.1',
])
for host in ALLOWED_HOSTS:
    if host and host not in ('*', 'localhost', '127.0.0.1', 'testserver'):
        clean_host = host.lstrip('.')
        origin = f"https://{clean_host}"
        if origin not in CSRF_TRUSTED_ORIGINS:
            CSRF_TRUSTED_ORIGINS.append(origin)


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Portfolio Apps
    'apps.accounts',
    'apps.portfolio',
    'apps.projects',
    'apps.services',
    'apps.skills',
    'apps.education',
    'apps.experience',
    'apps.certifications',
    'apps.achievements',
    'apps.blog',
    'apps.documents',
    'apps.contact',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'apps.portfolio.middleware.MaintenanceModeMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.portfolio.context_processors.global_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database Configuration (Supports Render PostgreSQL, SQLite with Persistent Storage, and MySQL)
DATABASE_URL = env('DATABASE_URL', default='')
DB_ENGINE = env('DB_ENGINE', default='sqlite')

if DATABASE_URL:
    # 1. Managed PostgreSQL or MySQL on Render via DATABASE_URL
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            conn_health_checks=True,
            ssl_require=False if ('localhost' in DATABASE_URL or '127.0.0.1' in DATABASE_URL) else True,
        )
    }
elif DB_ENGINE == 'mysql':
    # 2. Standalone MySQL with PyMySQL
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': env('DB_NAME', default='portfolio_db'),
            'USER': env('DB_USER', default='root'),
            'PASSWORD': env('DB_PASSWORD', default=''),
            'HOST': env('DB_HOST', default='127.0.0.1'),
            'PORT': env('DB_PORT', default='3306'),
            'OPTIONS': {
                'charset': 'utf8mb4',
            },
        }
    }
else:
    # 3. SQLite with Render Persistent Storage (/var/data), Vercel (/tmp), or local BASE_DIR
    import os
    import shutil
    env_data_dir = env('DATA_DIR', default='')
    if env_data_dir:
        DATA_DIR = Path(env_data_dir)
    elif Path('/var/data').is_dir():
        DATA_DIR = Path('/var/data')
    elif os.environ.get('VERCEL'):
        DATA_DIR = Path('/tmp')
        if not (DATA_DIR / 'db.sqlite3').exists() and (BASE_DIR / 'db.sqlite3').exists():
            try:
                shutil.copy(BASE_DIR / 'db.sqlite3', DATA_DIR / 'db.sqlite3')
            except Exception:
                pass
    else:
        DATA_DIR = BASE_DIR

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': DATA_DIR / 'db.sqlite3',
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalisation
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Media files (Render Persistent Storage, Vercel /tmp, or local BASE_DIR/media)
env_data_dir = env('DATA_DIR', default='')
if env_data_dir:
    MEDIA_ROOT = Path(env_data_dir) / 'media'
elif Path('/var/data').is_dir():
    MEDIA_ROOT = Path('/var/data/media')
elif os.environ.get('VERCEL'):
    MEDIA_ROOT = Path('/tmp/media')
else:
    MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'
MEDIA_ROOT.mkdir(parents=True, exist_ok=True)

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Auth
LOGIN_URL = '/portal/login/'
LOGIN_REDIRECT_URL = '/portal/dashboard/'
LOGOUT_REDIRECT_URL = '/portal/login/'

# File upload limits
DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024  # 10 MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024  # 10 MB

# Security (production-ready flags, safe with DEBUG=True too)
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'SAMEORIGIN'
