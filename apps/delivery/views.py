from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import DeliveryAssignment
from .serializers import DeliveryAssignmentSerializer
from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer
from apps.accounts.models import User

class AvailableOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(status='ready_for_delivery')

class AcceptOrderView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        if order.status == 'ready_for_delivery':
            order.status = 'in_transit'
            order.delivery_person = request.user
            order.save()
            return Response({'status': 'order accepted'})
        return Response(
            {'error': 'Order not available for delivery'},
            status=status.HTTP_400_BAD_REQUEST
        )

class MyDeliveriesView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(delivery_person=self.request.user)

class DeliveryStatusUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        if order.delivery_person != request.user:
            return Response(
                {'error': 'Not your delivery order'},
                status=status.HTTP_403_FORBIDDEN
            )
        order.status = request.data.get('status', order.status)
        order.save()
        return Response({'status': 'delivery status updated'})
