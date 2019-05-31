from django.db import models
from django.utils import timezone

class Link(models.Model):
    url = models.URLField(max_length=400)
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        if self.url == None:
            return "URL IS NULL"
        return self.url