from django.core.management.base import BaseCommand
from apps.accounts.models import User

class Command(BaseCommand):
    help = 'Creates initial users (admin, customer, delivery)'

    def handle(self, *args, **options):
        # Create or update admin user
        admin, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'role': User.ADMIN
            }
        )
        admin.set_password('admin123')
        admin.is_staff = True
        admin.is_superuser = True
        admin.save()

        # Create or update customer user
        customer, created = User.objects.get_or_create(
            username='customer',
            defaults={
                'email': 'customer@example.com',
                'role': User.CUSTOMER
            }
        )
        customer.set_password('customer123')
        customer.save()

        # Create or update delivery user
        delivery, created = User.objects.get_or_create(
            username='delivery',
            defaults={
                'email': 'delivery@example.com',
                'role': User.DELIVERY
            }
        )
        delivery.set_password('delivery123')
        delivery.save()

        self.stdout.write(self.style.SUCCESS('Successfully created initial users'))
