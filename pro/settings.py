# from pathlib import Path

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# # Quick-start development settings - unsuitable for production
# SECRET_KEY = 'django-insecure-i_!ulp(6#%r)$-z8o!))eu33j)p_x7$=npjfzd)$tccb4n(9*-'
# DEBUG = True
# ALLOWED_HOSTS = []

# # Application definition
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'rest_framework',
#     'corsheaders',  # <-- added CORS
#     'website',
#     'rest_framework.authtoken'
# ]
# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.TokenAuthentication',
#     ]
# }

# MIDDLEWARE = [
#     'corsheaders.middleware.CorsMiddleware',  # <-- must be at top
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'pro.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR/'templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'pro.wsgi.application'

# # Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'e_commerce',
#         'USER': 'root',
#         'PASSWORD': 'Lavanya$21',
#         'HOST': 'localhost',
#         'PORT': '3306'
#     }
# }
# AUTH_USER_MODEL='website.AuthUser'

# # Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
# ]

# # Internationalization
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# # Static files
# STATIC_URL = 'static/'

# # Default primary key field type
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # -----------------------------
# # CORS Settings for React Frontend
# # -----------------------------
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:5173",  # Vite default
# ]

# CORS_ALLOW_CREDENTIALS = True




from pathlib import Path
import os

# -------------------------------
# Base directory
# -------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------
# Security
# -------------------------------
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your_default_secret')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['django-fsd.onrender.com', 'localhost']

# -------------------------------
# Installed Apps
# -------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'website',
]

# -------------------------------
# Middleware
# -------------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pro.urls'
WSGI_APPLICATION = 'pro.wsgi.application'

# -------------------------------
# Templates
# -------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# -------------------------------
# Database (PostgreSQL)
# -------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'django_fsd_db_g7xq'),
        'USER': os.environ.get('POSTGRES_USER', 'django_fsd_db_g7xq_user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'srr6p5meZpjdlXI0Gr0rBxSwsxav5XmF'),
        'HOST': os.environ.get('POSTGRES_HOST', 'dpg-d3d3agggjchc739lur50-a.oregon-postgres.render.com'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
        'OPTIONS': {
            'sslmode': 'require',  # Enforces SSL for Render
        },
    }
}


# -------------------------------
# Custom user model
# -------------------------------
AUTH_USER_MODEL = 'website.AuthUser'

# -------------------------------
# Password validation
# -------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# -------------------------------
# Internationalization
# -------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------------------
# Static files
# -------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# -------------------------------
# Default primary key
# -------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------------------
# CORS (for React frontend)
# -------------------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Update with your frontend URL if deployed
]
CORS_ALLOW_CREDENTIALS = True

# -------------------------------
# REST Framework
# -------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}
