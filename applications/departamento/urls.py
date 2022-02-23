from django.contrib import admin
from django.urls import path
from . import views

app_name = "departamento_app"

urlpatterns = [
    path("lista_departamento/", views.DepartamentoListView.as_view(), name="lista_departamento"),
    path("nuevo_departamento/", views.NewDepartmentoView.as_view(), name="nuevo_departamento"),
]
