from django.urls import path
from . import views

urlpatterns = [
    path('', views.Fetch_Django,name='Fetch_Django'),
 
]
