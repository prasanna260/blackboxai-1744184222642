from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    CUSTOMER = 1
    ADMIN = 2
    DELIVERY = 3
    
    ROLE_CHOICES = (
        (CUSTOMER, 'Customer'),
        (ADMIN, 'Admin'),
        (DELIVERY, 'Delivery Person'),
    )
    
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=CUSTOMER)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"
