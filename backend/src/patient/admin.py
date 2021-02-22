from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'dob', 'phone', 'email', 
    'street', 'city', 'state', 'zipcode', 'photo_license', 'appointment')

# Register your models here.

admin.site.register(Patient, PatientAdmin)