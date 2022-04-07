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

## Shell de Django (ORM)
Ingresamos a la shell con
```
pipenv run python manage.py shell
```
El shell permite ejecutar python directamente dentro del servidor, e interactuar con la base de datos con métodos nativos.
Por ejemplo para hacer consultas:
```python
>>> from blog.models import Post
>>> Post.objects.all()
<QuerySet [<Post: Primer post>, <Post: Segundo Post>, <Post: Tercer Post>]>
>>>
```
[Ver Documentación](https://docs.djangoproject.com/en/4.0/topics/db/queries/)

Ejemplo, crear una nueva entrada desde el shell:
```python
>>> nuevo_post = Post.objects.create(title="Cuarto Post", content="Post creado desde el shell de Django")
```

## Vistas / URL's
Para agregar una vista a nuestra app, editamos su archivo views.py

```python
from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("Bienvenido a Django")
```

Y luego la enlazamos a la url deseada en urls.py

```python
from django.contrib import admin
from django.urls import path
from blog.views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
]
```

## Templates HTML
Dentro de la carpeta de la app, creamos la carpeta *templates/blog/home.html*
<br><b>El nombre de la carpeta *template* se debe respetar ya que es el mismo que se utiliza internamente para todas las apps</b>
<br>Luego cargamos el contenido HTML, para después renderizarla modificando views.py:
```python
from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "blog/home.html")
```

## Variables de contexto
Ahora buscamos trasladar nuestra app de blog a la vista web, para hacerlo editamos *views.py*:

```python
from django.shortcuts import render, HttpResponse
from .models import Post

def home(request):
    posts = Post.objects.all()                                  # Obtenemos todos los posts
    return render(request, "blog/home.html", {'posts': posts})  # Enviamos los posts a la plantilla
```

Y después lo mostramos en el template html usando variables de Django y lógica Jinja2:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portada</title>
</head>
<body>
    <h1>Bienvenido a Django</h1>
    {% for post in posts %}
        <h2>{{ post.title }}</h2>
        <p>{{ post.content }}</p>
    {% endfor %}
</body>
</html>
```

## Páginas dinámicas
Agregamos otra vista en *views.py*:

```python
def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, "blog/post.html", {'post': post}) 
```

Y creamos la nueva plantilla post.html:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{post.title}}</title>
</head>
<body>
    <h1>{{post.title}}</h1>
    <p>{{post.content}}</p>
</body>
</html>
```

Por último, agregamos en *urls.py* el enlace dinámico para que pase el id a la vista:

```python
from django.contrib import admin
from django.urls import path
from blog.views import home, post

urlpatterns = [
    path('', home),
    path('post/<int:id>', post), # <int:id> es una variable que se puede usar en la url
    path('admin/', admin.site.urls),
]
```

Ahora si vamos a http://127.0.0.1:8000/post/1 -> Nos muestra el primer post en el nuevo template
<br>
Para hacerlo dinámico, podemos ahora agregarlo como enlaces en la página home.html:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portada</title>
</head>
<body>
    <h1>Bienvenido a Django</h1>
    {% for post in posts %} 
        <h2>{{ post.title }}</h2>
        <p><a href="/post/{{ post.id }}">Ver...</a></p>
    {% endfor %}
</body>
</html>
```


