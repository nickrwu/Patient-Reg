from django.db import models
import os


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

# Create your models here.

# Initiating Patient Model
class Patient(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    dob = models.DateField(max_length=10)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=70, blank=False)

    # Address
    street = models.TextField()
    city = models.TextField()
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)

    photo_license = models.ImageField(upload_to='id_images', blank=True, null=True)
    appointment = models.DateTimeField()
    
    def _str_(self):
        return self.firstname