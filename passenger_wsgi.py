import sys, os 
cwd = os.getcwd() 
sys.path.append(cwd) 
sys.path.append(cwd + '/mysite') 
os.environ['DJANGO_SETTINGS_MODULE'] = "seventrans.settings" 
from django.core.wsgi import get_wsgi_application 
application = get_wsgi_application()