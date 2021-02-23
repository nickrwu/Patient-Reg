from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReactView, name= 'patients'),
]