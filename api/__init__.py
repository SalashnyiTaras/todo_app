""" api directory is one of the apps of this project. This app enables developers to query data accessing API-endpoints.

This package consist of following modules and directories:
    - apps.py
    - models.py
    - serializers.py
    - tests.py
    - urls.py
    - views.py
    - migrations - stores history of app's models

When creating this package following imports have been made:
    - import base.models.Task
    - from django rest_framework imported serializers, Response, api_view
    - from django.urls import path
    - from django.apps import AppConfig
"""