from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from backend.authenticate import customJWTAuthentication
from backend.utils import ResponseSuccess, ResponseBadRequest
from .serializer import RatingMovieByUserSerializer
from .models import Movie, Rating, Rating_Movie_By_User

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([customJWTAuthentication])
def get_movies(request):
    return ResponseSuccess(message="Hello, World!")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([customJWTAuthentication])
def post_rating(request):
    data = request.data
    serializer = RatingMovieByUserSerializer(data=data)
    if serializer.is_valid():
        movie_id = serializer.data['movie_id']
        user_id = request.user.id
        rating = serializer.data['rating']
        try:
            instance_1 = Rating_Movie_By_User.objects.get(user=user_id, movie=movie_id)
            if instance_1 is not None:
                instance_1.rating = rating
                instance_1.save()
        except Rating_Movie_By_User.DoesNotExist:
            Rating_Movie_By_User.objects.create(
                    user_id=user_id,
                    movie_id=movie_id,
                    rating=rating
             )
        try:
            instance_2 = Rating.objects.get(movie=movie_id)
            if instance_2 is not None:
                if rating == 1:
                    instance_2.one += 1
                elif rating == 2:
                    instance_2.two += 1
                elif rating == 3:
                    instance_2.three += 1
                elif rating == 4:
                    instance_2.four += 1
                elif rating == 5:
                    instance_2.five += 1
                instance_2.save()    
        except Rating.DoesNotExist:
             Rating.objects.create(
                    user_id=user_id,   
                    movie_id=movie_id,
                    one=rating if rating == 1 else 0,
                    two=rating if rating == 2 else 0,
                    three=rating if rating == 3 else 0,
                    four=rating if rating == 4 else 0,
                    five=rating if rating == 5 else 0,
                )
        else:   
            return ResponseSuccess(message="Rating successfully!")