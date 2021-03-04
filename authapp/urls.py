from django.urls import path, include
from django.conf.urls import url
from authapp import views


from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data["status_code"] = response.status_code

    return response


urlpatterns = [
    path("", include("djoser.urls")),
    url(r"^api-token-auth/", views.CustomAuthToken.as_view()),
    path("", include("djoser.urls.authtoken")),
    path("verifyemail/", views.verify_if_exist_email, name="verify email"),
]
