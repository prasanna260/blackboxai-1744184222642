from django.urls import path
from .views import ProductListCreateView, ProductDetailView, ProductCategoryView

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('category/<str:category>/', ProductCategoryView.as_view(), name='product-category'),
]
