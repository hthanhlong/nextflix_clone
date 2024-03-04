from django.contrib import admin
from .models import Movie, Rating,Rating_Movie_By_User

# Register your models here.
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Rating_Movie_By_User)