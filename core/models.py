from django.db import models
import urllib.request
import urllib
import json
from urllib.parse import quote

class Movie(models.Model):
    def __str__(self):
        return '{} ({})'.format(
            self.title, self.year)

    title = models.CharField(max_length=300)
    year = models.PositiveIntegerField()
    website = models.URLField(blank=True)

class GhibliMovies(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    director = models.CharField(max_length=10)
    producer = models.CharField(max_length=10)
    release_date = models.DateTimeField()
    rt_score = models.PositiveIntegerField()

    def __str__(self):
        return self.title