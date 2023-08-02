from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='home'),
    path('tasks/', views.taskList, name='task-list')
]