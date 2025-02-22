from django.urls import path
from . import views

urlpatterns = [
    path('tasks', views.tasks_template, name='tasks_template'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('state/<int:id>', views.state, name='state'),
]