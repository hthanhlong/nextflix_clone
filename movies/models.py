
from django.db import models
from core.models import User


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_thumbnail = models.TextField(blank=True)
    movie_url = models.TextField(blank=True)
    views_count = models.PositiveIntegerField(default=0)
    rating_point = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Rating(models.Model):
        one = models.PositiveIntegerField(default=0, null=True, blank=True)
        two = models.PositiveIntegerField(default=0, null=True, blank=True)
        three = models.PositiveIntegerField(default=0, null=True, blank=True)
        four = models.PositiveIntegerField(default=0, null=True, blank=True)
        five = models.PositiveIntegerField(default=0, null=True, blank=True)
        movie = models.ForeignKey(Movie, related_name='movie', on_delete=models.CASCADE)

        def __str__(self):
            return self.movie.title
        
class Rating_Movie_By_User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username