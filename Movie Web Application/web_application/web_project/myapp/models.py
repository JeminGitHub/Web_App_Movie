from django.db import models


# Create your models here.
class Movie(models.Model):

    name = models.CharField(max_length=250)
    desc = models.TextField(max_length=250)
    year = models.DateField()
    img = models.ImageField(upload_to='movies')

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()