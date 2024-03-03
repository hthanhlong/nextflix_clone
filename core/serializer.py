from .models import User
from rest_framework import serializers


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'first_name', 'last_name')

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


