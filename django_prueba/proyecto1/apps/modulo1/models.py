from django.db import models # type: ignore

# Create your models here.
from django.db import models # type: ignore

# Create your models here.

class modulo1(models.Model):
    nombre = models.CharField( max_length=20, null=False, unique=True)
    descripcion= models.TextField()
    imagen= models.ImageField(upload_to="modulo1", default="categorias/disco_default.png")
    fecha_agregado= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
       ordering=('fecha_agregado',) 