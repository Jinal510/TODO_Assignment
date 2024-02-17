from django.urls import path # Import the 'path' function from the Django URLs module
from . import views # Import views module from the current directory

urlpatterns = [
    path('', views.index, name='list'),# URL pattern for the base URL, directing to the 'index' view
    path('task-update/<str:pk>/', views.taskUpdate, name='task-update'), # URL pattern for task update, with a dynamic parameter 'pk', directing to the 'taskUpdate' view
    path('task-delete/<str:pk>/', views.taskDelete, name='task-delete'), #URL pattern for task delete, with a dynamic parameter 'pk', directing to the 'taskDelete' view
]
