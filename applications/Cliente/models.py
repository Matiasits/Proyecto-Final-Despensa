from django.db import models

# Create your models here.
class Cliente(models.Model):
    """Model definition for Cliente."""

    dni = models.IntegerField(primary_key=True)
    nombre = models.CharField("Nombre de cliente", max_length=50)
    apellido = models.CharField("Apellido de cliente", max_length=50)
    nombre_completo = models.CharField("Nombre Completo", max_length=50, default='')
    avatar = models.ImageField('imagen', upload_to='Cliente', height_field=None, width_field=None, max_length=None , blank=True)

    class Meta:
        """Meta definition for Cliente."""

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        """Unicode representation of Cliente."""
        return f"{self.dni}, {self.nombre}, {self.apellido}"