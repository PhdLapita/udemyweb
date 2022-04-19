from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=250)
    website = models.URLField(max_length=250)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
    
class Inmueble(models.Model):
    direccion = models.CharField(max_length=150)
    pais = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)
    imagen = models.CharField(max_length=900)
    active = models.BooleanField(default=True)
    empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE, related_name = "inmuebleslist")
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.direccion
    

class Comentario(models.Model):
    #comentario_user = models.ForeignKey(User, on_delete=models.CASCADE)
    calificacion = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    texto = models.CharField(max_length=200, null=True)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name="comentarios")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return str(self.calificacion) + " " + self.inmueble.direccion



