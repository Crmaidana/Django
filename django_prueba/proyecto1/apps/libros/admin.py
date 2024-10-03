from django.contrib import admin # type: ignore

from .models import Categoria, Libro # type: ignore

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Libro)