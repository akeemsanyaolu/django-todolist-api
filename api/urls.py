from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='home'),
    path('tasks/', views.taskList, name='task-list'),
    path('tasks/<int:pk>/', views.taskDetail, name='task-detail'),
    path('tasks/create/', views.taskCreate, name='task-create'),
    path('tasks/update/<int:pk>/', views.taskUpdate, name='task-update'),
    path('tasks/delete/<int:pk>/', views.taskDelete, name='task-delete'),
    
]