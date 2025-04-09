from rest_framework import serializers
from .models import Notification
from apps.orders.serializers import OrderSerializer
from apps.accounts.serializers import UserSerializer

class NotificationSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Notification
        fields = ['id', 'user', 'order', 'message', 'is_read', 'created_at']
        read_only_fields = ['created_at']
