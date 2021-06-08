"""
ASGI config for cs_raviolis project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import sys
from pathlib import Path

from django.core.asgi import get_asgi_application

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'cs_raviolis.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cs_raviolis.settings')

application = get_asgi_application()
