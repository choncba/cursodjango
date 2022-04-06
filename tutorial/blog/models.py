from tabnanny import verbose
from django.db import models

# Create your models here.

class Post(models.Model):
    # verbose_name cambia el rótulo de title y content
    title = models.CharField(max_length=100, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")

    # la clase meta permite cambiar el título de las entradas
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"

    # redefinimos __str__ para que nos devuelva el título
    def __str__(self):
        return self.title