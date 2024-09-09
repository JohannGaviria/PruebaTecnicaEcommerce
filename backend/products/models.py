from django.db import models


# Módelo de dato del producto
class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False) # Nombre del producto
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)  # Precio del producto
    availability = models.PositiveIntegerField(null=False, blank=False)  # Cantidad disponible del producto
    

    def __str__(self):
        return self.name
    

    # Verificar que el producto este disponible
    def is_available(self):
        return self.availability > 0