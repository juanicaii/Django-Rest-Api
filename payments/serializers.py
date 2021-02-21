from rest_framework import serializers
from .models import Order, Orders_Detail, Coupons
from products.models import Product
from authapp.models import User


class OrdersDetailsSerializer(serializers.ModelSerializer):
    productId = serializers.SlugRelatedField(
        queryset=Product.objects.all(),
        slug_field="id",
    )

    class Meta:
        model = Orders_Detail
        fields = ["id", "payments_type", "price", "productId"]


class OrdersSerializer(serializers.ModelSerializer):
    details = OrdersDetailsSerializer()
    customers = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="id",
    )

    class Meta:
        model = Order
        fields = ["number", "details", "quantity", "state", "date", "customers"]


class CouponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupons
        fields = "__all__"