from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="list"),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),    # when you visit the URL http://example.com/update_task/abc123/, Django will capture the string value abc123 from the URL and pass it as the pk parameter to the updateTask view function.
    path('delete_task/<str:pk>/', views.deleteTask, name='delete'),    
]
