""" Module urls.py maps django's urls and views (imported from current directory).

The idea behind this module is to match client's request to certain URL with a view function which handles
request further.

Mapping succeeds by virtue of import of path() from django.urls. Important to note that in this module
class-based views have been used. Using class-based views requires import and use of as.view() method.

After all imports have been made list of paths - urlpatterns can be created.

This module enables for client to access following URL: login, logout and register pages. Path for viewing, updating,
 deleting and creating model's object has been also set.

Each path() has also parameter name specified for recursive call of path function when needed, for instance from
Django's templates.
"""

from django.urls import path
from django.contrib.auth.views import LogoutView
from base import views

urlpatterns = [

    path('login/', views.TaskLoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('', views.TaskListView.as_view(), name='tasks'),
    path('task/<int:pk>', views.TaskDetailView.as_view(), name='task'),
    path('task-create/', views.TaskCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>', views.TaskUpdateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>', views.TaskDeleteView.as_view(), name='task-delete'),
]