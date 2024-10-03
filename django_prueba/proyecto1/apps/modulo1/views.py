from django.shortcuts import render # type: ignore

from django.urls import reverse_lazy # type: ignore

from .models import modulo1

from django.views.generic.edit import CreateView, UpdateView,DeleteView # type: ignore

class CrearRegistro(CreateView):
    model= modulo1
    fields={'nombre','descripcion'} # type: ignore
    template_name= 'modulo1/agregar_registro.html'
    success_url= reverse_lazy('index')
    
class ActualizarRegistro(UpdateView):   
    model= modulo1
    fields={'nombre','descripcion'} # type: ignore
    template_name= 'modulo1/agregar_registro.html'
    success_url= reverse_lazy('index')
    
class EliminarRegistro(DeleteView):   
    model= modulo1
    template_name= 'modulo1/eliminar_registro.html'
    success_url= reverse_lazy('index')
       
    

def mostrar_registros(request):
    registros = modulo1.objects.all()
    contexto = {
        "registros": registros
    }
    template='modulo1/listar_registros.html'  
      
    return render(request=request, template_name='template',context=contexto)

def mostrar_registros_by_id(request, id):
    registro=modulo1.objects.get(id)
    contexto = {
        "registro": registro
    }
    template='modulo1/detalle_modulo.html'  
      
    return render(request=request, template_name='template',context=contexto)
