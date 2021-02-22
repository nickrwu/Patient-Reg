"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from patient import views

router = routers.DefaultRouter()
# router.register(r'patients', views.PatientView, 'patient')

urlpatterns = [
    path('admin/', admin.site.urls),

    # Specifying URL path for API
    # path('api/', include(router.urls)),

    path('api/', include('patient.urls')),

    # path('api/', views.apiOverview, name="api-overview"),
    # path('api/patient-list/', views.patientList, name="patient-list"),
	# path('api/patient-info/<str:pk>/', views.patientInfo, name="patient-detail"),
	# path('api/patient-create/', views.patientCreate, name="patient-create"),

	# path('api/patient-update/<str:pk>/', views.patientUpdate, name="patient-update"),
	# path('api/patient-delete/<str:pk>/', views.patientDelete, name="patient-delete"),
]
