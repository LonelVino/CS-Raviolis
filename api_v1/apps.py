'''
/api_v1/apps.py
-------------------------
Entrance of the Page(root: user, cart, order, shop)
'''

from django.apps import AppConfig


class ApiV1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_v1'
