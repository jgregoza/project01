from dataclasses import field
import imp
from django.views.generic import TemplateView, ListView, CreateView

# Models

from .models import Prueba
from .forms import PruebaForm

# Create your views here.

class HomePageView(TemplateView):

    template_name = "home/index.html"


class HomeListView(ListView):

    template_name = "home/lista.html"
    context_object_name = 'lista_numeros'
    queryset = ['0', '10', '20', '30']


class PruebaListView(ListView):

    template_name = "home/model_lista.html"
    model = Prueba
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    template_name = "home/add_view.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/'


