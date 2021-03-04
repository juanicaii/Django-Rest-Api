from django.db import models
from django.contrib.auth.models import AbstractUser
from payments.models import Order
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserManager(BaseUserManager):
    def create_user(
        self,
        email,
        password,
        first_name,
        last_name,
    ):

        if not email:
            raise ValueError("Email is empty...")

        if not password or len(password) < 6:
            raise ValueError("Invalid password...")

        email = self.normalize_email(email)
        user = self.model(email=email, password=password, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
        self,
        email,
        password,
        first_name,
        last_name,
    ):
        user = self.create_user(email, password, last_name, first_name)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(verbose_name="Correo Electronico", max_length=255, unique=True)
    phone = models.CharField(verbose_name="Telefono", max_length=255, null=True, blank=True)
    address = models.CharField(verbose_name="Direccion", max_length=255, null=True, blank=True)

    REQUIRED_FIELDS = ["first_name", "last_name"]

    USERNAME_FIELD = "email"
    objects = UserManager()

    def get_username(self):
        return self.email

    get_username.short_description = "Correo Electronico"

    def get_first_name(self):
        return self.first_name

    get_first_name.short_description = "Nombre"

    def get_last_name(self):
        return self.last_name

    get_last_name.short_description = "Apellido"
