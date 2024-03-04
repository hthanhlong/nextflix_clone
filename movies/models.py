from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_thumbnail = models.TextField(blank=True)
    movie_url = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title