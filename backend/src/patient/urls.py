from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.PatientView.as_view(), name= 'patients_list'),
]