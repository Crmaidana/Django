from django.shortcuts import render # type: ignore
from django.urls import reverse_lazy # type: ignore
from django.views.generic.edit import CreateView, UpdateView, DeleteView # type: ignore
from django.views.generic.list import ListView # type: ignore
from .models import Categoria, Libro # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin # type: ignore
# Create your views here.
# ------- Categorias -----------------
class CrearCategoria(LoginRequiredMixin, CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'libros/agregar_categoria.html'
    success_url = reverse_lazy('index')
    
class ActualizarCategoria(UpdateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'libros/agregar_categoria.html'
    success_url = reverse_lazy('index')
    
class EliminarCategoria(DeleteView):
    model = Categoria
    template_name = 'generic/confirma_eliminar.html'
    success_url = reverse_lazy('index')
# ------- Libros -----------------
class CrearLibro(CreateView):
    model = Libro
    fields = ['titulo','autor','descripcion','categoria','imagen']
    template_name = 'libros/agregar_libro.html'
    success_url = reverse_lazy('index')
class ActualizarLibro(UpdateView):
    model = Libro
    fields = ['titulo','autor','descripcion','categoria','imagen']
    template_name = 'libros/agregar_libro.html'
    success_url = reverse_lazy('index')
class EliminarLibro(DeleteView):
    model = Libro
    template_name = 'generic/confirma_eliminar.html'
    success_url = reverse_lazy('index')
class ListarLibros(ListView):
    model = Libro
    template_name = 'libros/listar_libros.html'
    context_object_name = 'libros'