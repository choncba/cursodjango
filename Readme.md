## Crear un proyecto Django de cero
### Verificar tener instalado pipenv en el host (virtualenv y pip en un solo comando)
pip install pipenv
1 - Instalar Django con pipenv 
Crea el entorno virtual e instala paquetes de Django, a su vez crea el archivo Pipfile, donde se listan las dependencias (reemplaza a requeriments.txt). El entorno virtual se crea en una carpeta aparte (/user/.virtualenvs), no junto con el proyecto
pipenv install django
2 - Iniciar el proyecto en el entorno virtual
pipenv run django-admin startproject NOMBRE-DEL-PROYECTO
3 - Iniciamos el manager de Django
cd tutorial
pipenv run python manage.py runserver
Podemos ahora ver la web de trueba en el browser en http://127.0.0.1:8000/
