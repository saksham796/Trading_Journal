# WSGI entrypoint for the Django project
# This file proxies to the actual Django WSGI application located at
# Trading_Journal/Trading_Journal/wsgi.py to ensure gunicorn imports the
# correct module when using the path "Trading_Journal.wsgi:application".

from importlib import import_module

# Import the inner project's wsgi module and expose its `application`
_inner_wsgi = import_module('Trading_Journal.Trading_Journal.wsgi')
application = getattr(_inner_wsgi, 'application')