from django.contrib import admin
from .models import Post

# Agrega el modelo de nuestra App al panel de administracion
admin.site.register(Post)

