from django.contrib import admin
from .models import Product, Category, Size


# Register your models here.
class AdminProducts(admin.ModelAdmin):
    list_display = ("name", "get_description_elipsis", "stock", "long", "width", "weigth", "heigth")


class SizeAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


admin.site.register(Product, AdminProducts)
admin.site.register(Category)
admin.site.register(Size, SizeAdmin)
