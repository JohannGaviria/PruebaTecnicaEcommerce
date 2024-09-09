from django.core.management.base import BaseCommand
from faker import Faker
from products.models import Product


"""
python manage.py populate_products
"""
class Command(BaseCommand):
    help = 'Populate the database with realistic sample products'

    def handle(self, *args, **kwargs):
        fake = Faker()
        # Crea productos de muestra
        for _ in range(35):
            Product.objects.create(
                name=fake.word() + " " + fake.word(),
                price=fake.random_int(min=50, max=1500, step=50),
                availability=fake.random_int(min=0, max=100)
            )
        # Mensaje de éxito
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with realistic sample products'))
