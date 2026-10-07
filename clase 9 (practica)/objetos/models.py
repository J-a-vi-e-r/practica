from django.db import models

class Objeto(models.Model):
    nombre = models.CharField("Nombre de Objeto", max_length=100)
    descripcion = models.TextField("Descrición", blank=True)
    entregado = models.BooleanField("Entregado", default=False)

    def __str__(self):
        return self.nombre
