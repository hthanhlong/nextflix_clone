from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from backend.authenticate import customJWTAuthentication
from backend.utils import ResponseSuccess


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([customJWTAuthentication])
def get_movies(request):
    return ResponseSuccess(message="Hello, World!")