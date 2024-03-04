from rest_framework import serializers

class RatingMovieByUserSerializer(serializers.Serializer):
    movie_id = serializers.CharField()
    rating = serializers.IntegerField()

