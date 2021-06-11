""" Module urls.py maps django's urls and views.

The idea behind this module is to match client's request to certain URL with a view function which handles
request further.

Mapping succeeds by virtue of import of path() from django.urls. It is also necessary to import view from current app.

After all imports have been made it is time to create a list of paths - urlpatterns - where api endpoints
are created and function which handles logic for those endpoints were also given. Each path() has also parameter name
specified for recursive call of path function when needed, for instance from Django's templates.
"""

from django.urls import path
from api import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('task-list/', views.task_list, name='task-list'),
    path('task-details/<str:pk>/', views.task_details, name='task-details')
]
