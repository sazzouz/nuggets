from django.db import models
from taggit.managers import TaggableManager
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = TaggableManager()

    def __str__(self):
        return self.title