from django.urls import path
from .views import DeliveryAssignmentView, DeliveryStatusUpdateView

urlpatterns = [
    path('assignments/', DeliveryAssignmentView.as_view(), name='delivery-assignments'),
    path('assignments/<int:pk>/', DeliveryStatusUpdateView.as_view(), name='delivery-status'),
]
