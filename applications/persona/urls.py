from os import name
from django.contrib import admin
from django.urls import path
from . import views

app_name = "persona_app"  # Nombre de url's

urlpatterns = [
    path("", views.InicioView.as_view(), name="inicio"),
    path("create_empleado/", views.EmpleadoCreateView.as_view(), name="crear_empleado"),
    path("lista_empleados/", views.ListEmpleados.as_view(), name="lista_empleados"),
    path("lista_area/<name>/", views.ListEmpleadosArea.as_view(), name="empleado_area"),
    path("lista_area_admin/", views.ListEmpleadosAdmin.as_view(), name="empleado_admin"),
    path("update_view/<pk>/", views.EmpleadoUpdateView.as_view(), name="empleado_update"),
    path("delete_view/<pk>/", views.EmpleadoDeleteView.as_view(), name="empleado_delete"),
    # path('lista_job/<job>/', views.ListEmpleadosJob.as_view()),
    path("buscar_empleados/", views.ListBuscarEmpleados.as_view()),
    path("lista_skills/", views.ListaHabilidades.as_view(), name="habilidades"),
    path("detalle_empleado/<pk>/", views.EmpleadoDetailView.as_view(), name="empleado"),
    path("success_view/", views.SuccessView.as_view(), name="success"),
]
