from django.db import models

# Create your models here.
class Flyer(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='photos')
    description = models.CharField(max_length=100)
