""" This module provide functionality to register current app in order to make it accessible in admin page.

The main idea of this module is to make it possible to manipulate model's objects via admin page. To do so, it is
necessary to import admin from django.contrib and to pass a model of current app into admin.site.register(). After that
it is possible to delete, create, update, view objects of Task model from admin site.
"""

from django.contrib import admin
from base.models import Task

admin.site.register(Task)
