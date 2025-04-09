from rest_framework import serializers
from .models import DeliveryAssignment

class DeliveryAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAssignment
        fields = ['id', 'order', 'assigned_to', 'status', 'assigned_at', 'updated_at']
        read_only_fields = ['id', 'assigned_at', 'updated_at']
