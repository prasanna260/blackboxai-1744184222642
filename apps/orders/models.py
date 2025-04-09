from django.db import models
from apps.accounts.models import User
from apps.products.models import Product

class Order(models.Model):
    PENDING = 1
    PACKED = 2
    OUT_FOR_DELIVERY = 3
    DELIVERED = 4
    CANCELLED = 5
    
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (PACKED, 'Packed'),
        (OUT_FOR_DELIVERY, 'Out for Delivery'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
    )
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=PENDING)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Order #{self.id} - {self.customer.get_full_name()}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity}x {self.product.name} for Order #{self.order.id}"
