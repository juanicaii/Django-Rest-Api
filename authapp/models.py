from django.db import models
from django.contrib.auth.models import AbstractUser
from payments.models import Order

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(verbose_name="Correo Electronico", max_length=255, unique=True)
    phone = models.CharField(verbose_name="Telefono", max_length=255, null=True, blank=True)
    address = models.CharField(verbose_name="Direccion", max_length=255, null=True, blank=True)

    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    USERNAME_FIELD = "email"

    def get_username(self):
        return self.email

    get_username.short_description = "Correo Electronico"

    def get_first_name(self):
        return self.first_name

    get_first_name.short_description = "Nombre"

    def get_last_name(self):
        return self.last_name

    get_last_name.short_description = "Apellido"
