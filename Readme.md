## Crear un proyecto Django de cero
### Verificar tener instalado pipenv en el host (virtualenv y pip en un solo comando)

pip install pipenv
<br>1 - Instalar Django con pipenv 
Crea el entorno virtual e instala paquetes de Django, a su vez crea el archivo Pipfile, donde se listan las dependencias (reemplaza a requeriments.txt). El entorno virtual se crea en una carpeta aparte (/user/.virtualenvs), no junto con el proyecto
pipenv install django
<br>2 - Iniciar el proyecto en el entorno virtual:
```
pipenv run django-admin startproject NOMBRE-DEL-PROYECTO
```
3 - Iniciamos el manager de Django
```
cd tutorial
pipenv run python manage.py runserver
```
Podemos ahora ver la web de trueba en el browser en [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

* Para iniciar más fácil el server, podemos agragar el siguiente script al final de Pipfile:
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
```
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
```
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