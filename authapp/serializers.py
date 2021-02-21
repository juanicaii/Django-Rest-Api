from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import User


class UserCreateSerializerF(UserCreateSerializer):
    class Meta(UserSerializer):
        model = User
        fields = ("id", "email", "username", "password", "first_name", "last_name")
