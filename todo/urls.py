""" The `urlpatterns` list routes URLs to views. For more information: https://docs.djangoproject.com/en/3.2/topics/http/urls/

This module can be considered as main router as this module separates URL of projects app: api and base. Client's
requests starting with '/' will be redirected to urls-module of base app and requests starting with "api" will be
redirected to api's urls-module. To provide such a functionality from django-urls have been imported functions path
and include.

This module also registers a route for admin-page (importing admin from django.contrib). Logging to a admin site
allows user to perform management actions.

Last but not least, to the urlpatterns has been added path for uploading/storing/downloading media files by user when
debug mode is on. To achieve this result, setting have been imported from django.conf and static() was imported from
django.conf.urls.static.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    # if DEBUG=True, add static path
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
