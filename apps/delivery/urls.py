from django.urls import path
from .views import (
    AvailableOrdersView,
    AcceptOrderView,
    MyDeliveriesView,
    DeliveryStatusUpdateView
)

urlpatterns = [
    path('available/', AvailableOrdersView.as_view(), name='available-orders'),
    path('accept/<int:pk>/', AcceptOrderView.as_view(), name='accept-order'),
    path('my-deliveries/', MyDeliveriesView.as_view(), name='my-deliveries'),
    path('update-status/<int:pk>/', DeliveryStatusUpdateView.as_view(), name='update-delivery-status'),
]
