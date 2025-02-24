from .base import *

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': os.getenv("dbengine"),
        'NAME': os.getenv("dbname"),
        'USER': os.getenv("user"),
        'PASSWORD': os.getenv("password"),
        'HOST': os.getenv("host"),
        'PORT': os.getenv("port")
    }
}