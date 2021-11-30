from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    poster = models.CharField(max_length=200)
    trailer = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    release_year = models.IntegerField()
    