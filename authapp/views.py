from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


# Create your views here.


# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def restricted(request, *args, **kwargs):
#     return Response(data="Only for Logged in User", status=status.HTTP_200_OK)
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):

        if request.auth == None:
            serializer = self.serializer_class(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "access_token": token.key,
                    "id": user.pk,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "message": "Ya estas Logeado",
            },
            status=status.HTTP_200_OK,
        )


@api_view(["POST"])
def verify_if_exist_email(request):
    print(request.data)
    user = get_user_model().objects.filter(email=request.data["email"])
    if not user:
        return Response(
            {
                "message": "Se puede utilizar",
            },
            status=status.HTTP_200_OK,
        )
    else:
        return Response(
            {
                "message": "Ya esta en uso",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
