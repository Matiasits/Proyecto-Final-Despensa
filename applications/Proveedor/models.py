from django.db import models

# Create your models here.
class Proveedor(models.Model):
    """Model definition for Proveedor."""

    identificador = models.IntegerField(primary_key=True)
    nombre = models.CharField("Nombre del proveedor", max_length=50)
    rubro = models.CharField("Rubro del proveedor", max_length=50)


    class Meta:
        """Meta definition for Proveedor."""

        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        """Unicode representation of Proveedor."""
        return f"{self.identificador}, {self.nombre}, {self.rubro}"