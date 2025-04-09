from rest_framework import generics, permissions
from .models import DeliveryAssignment
from .serializers import DeliveryAssignmentSerializer

class DeliveryAssignmentView(generics.ListCreateAPIView):
    queryset = DeliveryAssignment.objects.all()
    serializer_class = DeliveryAssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class DeliveryStatusUpdateView(generics.RetrieveUpdateAPIView):
    queryset = DeliveryAssignment.objects.all()
    serializer_class = DeliveryAssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]
