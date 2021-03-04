from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserCreateSerializerF:
    class Meta:
        model = User
        fields = "first_name"
