from django.contrib import admin
from .models import Coupons, Order, Orders_Detail


class OrderDetailsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        # Return nothing to make sure user can't update any data
        pass


class OrderAdmin(admin.ModelAdmin):

    list_display = ("number", "get_customer", "get_detail_product", "get_detail_price", "state", "date")
    list_filter = ("date",)
    search_fields = ("get_customer", "get_detail_product")

    def has_add_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        # Return nothing to make sure user can't update any data
        pass

    def get_customer(self, obj):
        return obj.customers.email

    def get_detail_product(self, obj):
        return obj.details.productId.name

    def get_detail_price(self, obj):
        return "$ " + str(obj.details.price)

    get_customer.short_description = "Cliente"
    get_detail_product.short_description = "Producto"
    get_detail_price.short_description = "Precio"


class CouponAdmin(admin.ModelAdmin):
    list_display = ("name", "discount")


admin.site.register(Order, OrderAdmin)
admin.site.register(Orders_Detail, OrderDetailsAdmin)
admin.site.register(Coupons, CouponAdmin)
