from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from apps.products.models import Product
from apps.accounts.models import User

class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == User.ADMIN:
            return Order.objects.all()
        return Order.objects.filter(customer=user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

class OrderDetailView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        return [permissions.IsAdminUser()]

    def get_queryset(self):
        user = self.request.user
        if user.role == User.ADMIN:
            return Order.objects.all()
        return Order.objects.filter(customer=user)
