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
