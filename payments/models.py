from django.db import models
import uuid
from django.utils import timezone
from products.models import Product


# Create your models here.


class Coupons(models.Model):
    name = models.CharField(verbose_name="Cupon", max_length=50)
    discount = models.FloatField(verbose_name="Descuento en %")

    class Meta:
        verbose_name = "Cupon"
        verbose_name_plural = "Cupones"

    def __str__(self) -> str:
        return self.name


class Orders_Detail(models.Model):
    payments_type = models.CharField(verbose_name="Tipo de Pago", max_length=50)
    productId = models.ForeignKey(
        Product, verbose_name="Productos Comprados", related_name="products", on_delete=models.CASCADE
    )
    quantity = models.IntegerField(verbose_name="Cantidad", default=1)
    price = models.FloatField(verbose_name="Precio")

    def __str__(self) -> str:
        return str(self.pk)

    class Meta:
        verbose_name = "Detalle"
        verbose_name_plural = "Detalles "


class Order(models.Model):
    number = models.UUIDField(verbose_name="Numero de Orden", primary_key=True, default=uuid.uuid4, editable=False)
    state = models.BooleanField(verbose_name="Estado de la Orden", default=False)
    details = models.OneToOneField(
        Orders_Detail, related_name="detail", verbose_name="Detalle de la Orden", on_delete=models.CASCADE
    )
    date = models.DateTimeField(verbose_name="Fecha de la Orden", default=timezone.now)
    customers = models.ForeignKey(
        "authapp.User", verbose_name="Clientes", on_delete=models.CASCADE, blank=True, null=True, default=None
    )

    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Ordenes"

    def __str__(self) -> str:
        return str(self.number)