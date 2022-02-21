from django.db import models
from django.forms import CharField
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.


class Habilidades(models.Model):
    habilidad = models.CharField("Habilidad", max_length=50)

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades Empleados"

    def __str__(self):
        return self.habilidad


class Empleado(models.Model):
    JOB_CHOISES = (
        ("0", "Contador"),
        ("1", "Administrador"),
        ("2", "Economista"),
        ("3", "Otro"),
    )
    first_name = models.CharField("Nombres", max_length=60)
    last_name = models.CharField("Apellidos", max_length=60)
    full_name = models.CharField("Nombres completos", max_length=120, blank=True)
    job = models.CharField("Trabajo", max_length=1, choices=JOB_CHOISES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    resume = RichTextField()

    class Meta:
        verbose_name = "Mi empleado"
        verbose_name_plural = "Empleados de la empresa"
        ordering = ["-first_name", "last_name"]
        unique_together = ("first_name", "departamento")

    def __str__(self):
        return self.first_name
