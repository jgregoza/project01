from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Alias', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False)

    def __str__(self):
        return self.name
