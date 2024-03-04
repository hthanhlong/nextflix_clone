from django.urls import path
from .views import get_movies, post_rating

urlpatterns = [
    path('movies', get_movies, name='get_movies'),
    path('movies/rating', post_rating, name='post_rating'),
]
