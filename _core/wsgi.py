#  wsgi = web server gateway interface

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '_core.settings.production')

application = get_wsgi_application()
app = application