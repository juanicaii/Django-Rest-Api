from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from authapp.permissions import isAdminOrReadOnly
from .models import Order, Orders_Detail, Coupons
from authapp.models import User
from .serializers import OrdersSerializer, CouponsSerializer
from products.models import Product
from .mercadopago import buy, mp


# Create your views here.


class ListOrders(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = (isAdminOrReadOnly,)

    def create(self, request):
        data = request.data
        print(data)
        product = Product.objects.filter(id=data["details"]["productId"])
        customer = User.objects.filter(id=data["customers"])
        if product:
            order_detail = Orders_Detail(
                payments_type=data["details"]["payments_type"], price=data["details"]["price"], productId=product[0]
            )
            order_detail.save()
            order = Order(details=order_detail, customers=customer[0], date=data["date"])
            order.save()
            url = buy(product[0].name, int(data["details"]["price"]), 1, str(order.number))["response"]["init_point"]
            return Response(data={"url": url}, status=status.HTTP_200_OK)
        else:
            return Response(data="El producto ingresado no existe", status=status.HTTP_400_BAD_REQUEST)


class DetailsOrders(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrdersSerializer


class PaymentSuccess(APIView):
    def get(self, request, format=None):
        payment_id = request.GET.get("payment_id")
        if payment_id:
            pago = mp.get_payment(payment_id)["response"]
            if pago["status"] == 404:
                return Response(data="No existe esa compra", status=status.HTTP_400_BAD_REQUEST)

            order = Order.objects.filter(number=pago["external_reference"]).update(state=True)
            return Response(data="Compra Completada", status=status.HTTP_200_OK)
        return Response(data="No tienes Permiso", status=status.HTTP_403_FORBIDDEN)


class ListCoupon(generics.ListCreateAPIView):
    queryset = Coupons.objects.all()
    serializer_class = CouponsSerializer


class DetailsCoupon(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrdersSerializer