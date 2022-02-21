from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.
admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):  # Modificar el view de Admin
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        'id',
    )

    # Agregar un campo personalizado; que no aparece en los modelos:

    def full_name(self, obj):
        return obj.first_name + " " + obj.last_name
        #return f"{obj.first_name} {obj.last_name}"


    # Filtros en el Admin
    search_fields = ('first_name',)
    list_filter = ('departamento', 'job', 'habilidades')
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)
