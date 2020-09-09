from django.db import models

# Create your models here.

class IMG(models.Model):

    img = models.ImageField(upload_to='booktest/')

    #name = models.CharField(max_length=200)