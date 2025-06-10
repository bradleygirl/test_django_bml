import os
from django.core.wsgi import get_wsgi_application
#from django.core.handlers.wsgi import WSGIHandler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogmaker_lite.settings")
application = get_wsgi_application()
#application = WSGIHandler()