from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('ORDER', 'Order Update'),
        ('DELIVERY', 'Delivery Update'),
        ('SYSTEM', 'System Notification'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    related_id = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.get_notification_type_display()} for {self.user}"

    class Meta:
        ordering = ['-created_at']
