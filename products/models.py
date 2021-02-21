from django.db import models
from uuid import uuid4
import os

# Create your models here.


def path_and_rename(instance, filename):
    ext = filename.split(".")[-1]
    if instance.pk:
        filename = "{}.{}".format(uuid4().hex, ext)
        return os.path.join("productos/", filename)


class Category(models.Model):

    name = models.CharField(verbose_name="Nombre de la Categoria", max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Size(models.Model):
    name = models.CharField(verbose_name="Nombre del Tamaño", max_length=255)
    price = models.FloatField(verbose_name="Precio")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tamaño"
        verbose_name_plural = "Tamaños"


class Product(models.Model):
    name = models.CharField(verbose_name="Nombre del Producto", max_length=255)
    img = models.ImageField(
        upload_to=path_and_rename,
        verbose_name="Imagen del Producto",
    )
    description = models.TextField(verbose_name="Descripcion del Producto")
    heigth = models.FloatField(verbose_name="Altura del Producto (cm)")
    width = models.FloatField(verbose_name="Ancho del Producto (cm)")
    long = models.FloatField(verbose_name="Largo del Producto (cm)")
    weigth = models.FloatField(verbose_name="Peso del Producto (kg)")
    stock = models.IntegerField(verbose_name="Stock del Producto")
    categoryId = models.ManyToManyField(Category, related_name="categories")
    sizeId = models.ManyToManyField(Size, related_name="sizes")

    def __str__(self):
        return self.name

    def get_description_elipsis(self):
        desc = str(self.description)
        return desc[0:80] + "..."

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    get_description_elipsis.short_description = "Descripcion del Producto"
