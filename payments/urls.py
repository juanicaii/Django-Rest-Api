from django.contrib import admin
from django.urls import path, include
from .views import ListOrders, DetailsOrders, PaymentSuccess, ListCoupon, DetailsCoupon


urlpatterns = [
    path("payment/", ListOrders.as_view(), name="Pago"),
    path("payment/<uuid:number>/", DetailsOrders.as_view(), name="Detalle de la Orden"),
    path("payment/success", PaymentSuccess.as_view(), name="Pago Exitoso"),
    path("coupons/", ListCoupon.as_view(), name="Cupones"),
    path("coupons/<int:pk>", DetailsCoupon.as_view(), name="Cupon"),
]
