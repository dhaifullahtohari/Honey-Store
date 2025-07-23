from pathlib import Path
import os
import cloudinary

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح التشفير (⚠️ لا تستخدمه كما هو في الإنتاج)
SECRET_KEY = 'django-insecure-k2czfp44glh9!(^^jy%no*&gagn#9movpim@(ov*p)&dipuku3'

# وضع التطوير
DEBUG = True

# المضيفون المسموح لهم
ALLOWED_HOSTS = []

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # خدمات Cloudinary
    'cloudinary',
    'cloudinary_storage',

    # تطبيقات المشروع
    'catalog',
    'accounts',
    'cart',
    'orders',
]

# الوسيطات (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ملف الروابط الرئيسي
ROOT_URLCONF = 'HoneyStore.urls'

# إعداد القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # مجلد القوالب العام
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# إعداد WSGI
WSGI_APPLICATION = 'HoneyStore.wsgi.application'

# قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# اللغة والمنطقة الزمنية
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# إعداد static
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# إعداد Cloudinary لتخزين ملفات media
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dq4ntpesw',
    'API_KEY': '873815379615733',
    'API_SECRET': 'qk1vJ94gOOQ9pefYKM1CwKMDhbU',  # ⚠️ للتطوير فقط
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# تفعيل إعداد Cloudinary عند تشغيل المشروع
cloudinary.config(
    cloud_name=CLOUDINARY_STORAGE['CLOUD_NAME'],
    api_key=CLOUDINARY_STORAGE['API_KEY'],
    api_secret=CLOUDINARY_STORAGE['API_SECRET']
)

# المفتاح الافتراضي للحقول التلقائية
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
