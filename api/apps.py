""" This module makes possible for Django to load/access api app.

The idea behind this module is that after api app is created, it is necessary to register app in projects' settings.py
INSTALLED_APPS list. To do so, class AppConfig was imported from django.apps. App registration succeeds via inheritance
from AppConfig a class of api - ApiConfig is created.
"""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """ A class used to register api app in projects' settings. Class inherits from AppConfig.

    Attributes:
    ----------
    default_auto_field : str
        defines apps' auto field
    name : str
        name of current app
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
