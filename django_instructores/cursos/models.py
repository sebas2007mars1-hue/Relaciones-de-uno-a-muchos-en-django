from django.db import models

# Create your models here.
from instructores.models import Instructor

class Curso(models.Model):

    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE
    )

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_horas = models.PositiveIntegerField()
    fecha_inicio = models.DateField()

    def __str__(self):
        return self.nombre