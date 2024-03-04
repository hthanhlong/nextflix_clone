from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .serializer import UserSignupSerializer, UserLoginSerializer
from .models import User
from .utils import generate_random_string, generate_token
from backend.utils import ResponseSuccess, ResponseBadRequest, generate_otp

@api_view(['POST'])
def login(request):
    data = request.data
    serializer = UserLoginSerializer(data=data)
    if not serializer.is_valid():
        return ResponseBadRequest(message="Invalid data!")
    try:
        user = User.objects.get(email=data['email'])
        if user:
            pass
            if user.is_authenticated == False:
                return ResponseBadRequest(
                    message="User not verified!"
                )
            password = make_password(data['password'], salt=user.salt)
            if password == user.password:
                tokens = generate_token(user)
                user_id = user.id
                return ResponseSuccess(
                    message="Login successful!",
                    data={
                        "user_id": user_id,
                        "tokens": tokens
                    }
                )
            else:
                return ResponseBadRequest(
                    message="Invalid password!"
                )
        else:
            return ResponseBadRequest(message="User not found!")
    except User.DoesNotExist:
        return ResponseBadRequest(message="User not found!")    
   

@api_view(['POST'])
def signup(request):
    data = request.data
    serializer = UserSignupSerializer(data=data)
    if serializer.is_valid():
        role_id = data['role'] if 'role' in data else 7
        salt = generate_random_string()
        hashed_password = make_password(data['password'], salt=salt)
        otp_code = generate_otp()
        User.objects.create(
            email=data['email'],
            password=hashed_password,
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            salt=salt,
            role_id=role_id,
            otp_code=otp_code
        )
        return ResponseSuccess(
            message="User created successfully!",
            status=status.HTTP_201_CREATED
        )
    else:
        return ResponseBadRequest(
            message="Invalid data!",
            data=serializer.errors
        )   
        
@api_view(['POST'])
def verify_otp(request):
    data = request.data
    user = User.objects.get(email=data['email'])
    if user:
        if user.otp_code == data['otp_code']:
            user.is_authenticated = True
            user.save()
            return ResponseSuccess(
                message="User verified successfully!"
            )
        else:
            return ResponseBadRequest(
                message="Invalid OTP!"
            )
    else:
        return ResponseBadRequest(
            message="User not found!"
        )
