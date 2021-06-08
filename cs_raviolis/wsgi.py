"""
WSGI config for cs_raviolis project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'YOURAPP.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cs_raviolis.settings')

application = get_wsgi_application()
