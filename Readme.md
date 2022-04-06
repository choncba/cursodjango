# Tutorial Django 
## Crear un proyecto Django de cero
### Verificar tener instalado pipenv en el host (virtualenv y pip en un solo comando)

```
pip install pipenv
```
1 - Instalar Django con pipenv 
Crea el entorno virtual e instala paquetes de Django, a su vez crea el archivo Pipfile, donde se listan las dependencias (reemplaza a requeriments.txt). El entorno virtual se crea en una carpeta aparte (/user/.virtualenvs), no junto con el proyecto
pipenv install django

<br>2 - Iniciar el proyecto en el entorno virtual:
```
pipenv run django-admin startproject NOMBRE-DEL-PROYECTO
```
Esto crea automáticamente la estructura básica del proyecto en Django y valores por default:
<br>
```
NOMBRE-DEL-PROYECTO/
    |
    |- NOMBRE-DEL-PROYECTO/
    |   |- __init__.py
    |   |- asgi.py
    |   |- settings.py 
    |   |- urls.py
    |   |- wsgi.py
    |
    |- db.sqlite3
    |- manage.py

Pipfile
```
3 - Iniciamos el manager de Django
```
cd tutorial
pipenv run python manage.py runserver
```
Podemos ahora ver la web de trueba en el browser en [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

* Para iniciar más fácil el server, podemos agregar el siguiente script al final de Pipfile:
```
[scripts]
server = "python manage.py runserver"
```
Después en a consola hacemos directamente
```
pipenv run server
```
4 - Crear una app:
```
pipenv run python manage.py startapp <NOMBRE_DE_LA_APP>
```
* Para activar la app recién creada, agregar el nombre de la app (<b>blog</b> en este caso) en el archivo settings.py del proyecto:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog'
]
```

5 - Creamos el modelo de nuestra app que se almacenará en la base de datos editando el archivo models.py de la app:
```python
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
```
Para que los cambios tomen efecto en la estructura del servidor, usamos el comando <b>makemigrations</b>:
```
pipenv run python manage.py makemigrations
```
Después usamos el comando <b>migrate</b> para integrarlo a la base de datos:
```
pipenv run python manage.py migrate
```
Los cambios se almacenan en la carpeta migrate de la app, de esta forma es posible revertirlos

6 - Consola de administrador de Django
Iniciar el servidor (Paso 3) y luego ir a la URL http://127.0.0.1:8000/admin
<br>Para ingresar debemos crear un usuario administardor:
```
pipenv run python manage.py createsuperuser
```
Completamos los campos para crearlo.

7 - Agregamos el modelo de nuestra app en *carpeta_de_la_app/admin.py*:
```python
from django.contrib import admin
from .models import Post

# Agrega el modelo de nuestra App al panel de administracion
admin.site.register(Post)
```

Ahora vemos el modelo agregado y la posibilidad de insertar entradas en el panel de administrador.

8 - Customizar rótulos del modelo modificando models.py de nuestra app:
```python
class Post(models.Model):
    # verbose_name cambia el rótulo de title y content
    title = models.CharField(max_length=100, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")

    # la clase Meta permite cambiar propiedades del modelo
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"

    # redefinimos __str__ para que nos devuelva el título
    def __str__(self):
        return self.title
```

## Shell de Django
Ingresamos a la shell con
```
pipenv run python manage.py shell
```
El shell permite ejecutar python directamente dentro del servidor, por ejemplo para hacer consultas:
```python
>>> from blog.models import Post
>>> Post.objects.all()
<QuerySet [<Post: Primer post>, <Post: Segundo Post>, <Post: Tercer Post>]>
>>>
```