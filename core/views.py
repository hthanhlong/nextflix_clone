from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .serializer import UserSignupSerializer, UserLoginSerializer
from .models import User
from .utils import generate_random_string
# Create your views here.

@api_view(['POST'])
def login(request):
    data = request.data
    serializer = UserLoginSerializer(data=data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.get(email=data['email'])
    if user:
        password = make_password(data['password'], salt=user.salt)
        if password == user.password:
            return Response({"message": "Login successful!"})
        else:
            return Response({"message": "Invalid password!"})
    else:
        return Response({"message": "User not found!"})

@api_view(['POST'])
def signup(request):
    data = request.data
    serializer = UserSignupSerializer(data=data)
    if serializer.is_valid():
        role_id = 7
        salt = generate_random_string()
        hashed_password = make_password(data['password'], salt=salt)
        User.objects.create(
            email=data['email'],
            password=hashed_password,
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            salt=salt,
            role_id=role_id
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       