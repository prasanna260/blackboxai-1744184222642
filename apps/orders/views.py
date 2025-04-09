from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer, OrderStatusSerializer
from apps.products.models import Product
from apps.accounts.models import User
from rest_framework.decorators import action

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

class CancelOrderView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        if order.status not in ['completed', 'cancelled']:
            order.status = 'cancelled'
            order.save()
            return Response({'status': 'order cancelled'})
        return Response(
            {'error': 'Order cannot be cancelled'},
            status=status.HTTP_400_BAD_REQUEST
        )

class AdminOrderManagementView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderStatusSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        order = self.get_object()
        serializer = OrderStatusSerializer(data=request.data)
        if serializer.is_valid():
            order.status = serializer.validated_data['status']
            order.save()
            return Response({'status': 'order status updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminDashboardView(generics.GenericAPIView):
    permission_classes = [permissions.IsAdminUser]
    
    def get(self, request):
        from django.db.models import Count, Sum
        from datetime import date, timedelta
        
        # Order status counts
        status_counts = Order.objects.values('status').annotate(
            count=Count('id')
        ).order_by('status')
        
        # Recent 30 days sales
        thirty_days_ago = date.today() - timedelta(days=30)
        recent_sales = Order.objects.filter(
            created_at__gte=thirty_days_ago,
            status=Order.DELIVERED
        ).aggregate(
            total_sales=Sum('total_amount'),
            order_count=Count('id')
        )
        
        # Top products
        top_products = OrderItem.objects.values(
            'product__name'
        ).annotate(
            total_ordered=Sum('quantity')
        ).order_by('-total_ordered')[:5]
        
        data = {
            'order_status_counts': status_counts,
            'recent_sales': recent_sales,
            'top_products': top_products
        }
        
        return Response(data)
