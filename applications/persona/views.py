from multiprocessing import context
from pyexpat import model
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)

# models
from applications.departamento.models import Departamento
from .models import Empleado
# forms
from .forms import EmpleadoForm


# Create your views here.

class InicioView(TemplateView):
    template_name = 'inicio.html'


class EmpleadoCreateView(CreateView):
    template_name = "persona/create_empleado.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy("persona_app:empleado_admin")  # Se redirecciona a la url con nombre 'success'

    def form_valid(self, form):  # Metodo que valida el post para guardarlo en la bd
        # logica del proceso
        empleado = form.save()
        empleado.full_name = empleado.first_name + " " + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class ListEmpleados(ListView):
    template_name = "persona/lista_empleados.html"
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", "")
        lista = Empleado.objects.filter(full_name__icontains=palabra_clave)
        return lista    
        

class ListEmpleadosArea(ListView):
    template_name = "persona/lista_area.html"
    context_object_name = 'empleados'


    def get_queryset(self):
        area = self.kwargs["name"]
        lista = Empleado.objects.filter(departamento__name=area)
        return lista


class ListEmpleadosAdmin(ListView):
    template_name = "persona/lista_area_admin.html"
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado


class EmpleadoUpdateView(UpdateView):
    template_name = "persona/empleado_update.html"
    model = Empleado
    fields = ["first_name", "last_name", "job", "departamento", "habilidades"]
    success_url = reverse_lazy("persona_app:empleado_admin")

    def post(self, request, *args, **kwargs):  # Metodo que intercepta el post desde el html antes de validarlo
        self.object = self.get_object()
        print("======METODO post======")  # identificar el orden en que se ejecutan y validan metodos
        print("=====PARAMETRO request=======")
        print(request.POST)  # muestra un diccionario con los datos del post
        print(request.POST["last_name"])  # recupera el valor de 'last_name'
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print("======METODO form_valid======")  # identificar el orden en que se ejecutan y  validan metodos
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    template_name = "persona/empleado_delete.html"
    model = Empleado
    success_url = reverse_lazy("persona_app:empleado_admin")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detalle_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del Mes'
        return context

        
# """class ListEmpleadosJob(ListView):
#     template_name = 'persona/lista_job.html'
   

#     def get_queryset(self):
#         area = self.kwargs['job']
#         lista = Empleado.objects.filter(
#         job = area 
#     )
#         return lista"""


# class ListBuscarEmpleados(ListView):
#     template_name = "persona/buscar_empleados.html"
#     context_object_name = "empleados"

#     def get_queryset(self):
#         palabra_clave = self.request.GET.get("kword", '')
#         lista = Empleado.objects.filter(
#             first_name=palabra_clave
#         )
#         return lista


# class ListaHabilidades(ListView):
#     template_name = "persona/lista_skills.html"
#     paginate_by = 4
#     ordering = "habilidades"
#     context_object_name = "habilidad"

#     def get_queryset(self):
#         empleado = Empleado.objects.get(id=2)
#         return empleado.habilidades.all()

    
# class SuccessView(TemplateView):
#     template_name = "persona/success_view.html"

