from django.urls import path
from .views import (
    OrderListCreateView,
    OrderDetailView,
    CancelOrderView,
    AdminOrderManagementView,
    AdminDashboardView
)

urlpatterns = [
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('<int:pk>/cancel/', CancelOrderView.as_view(), name='cancel-order'),
    path('admin/<int:pk>/manage/', AdminOrderManagementView.as_view(), name='admin-manage-order'),
    path('admin/dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
]
