from django.shortcuts import render, HttpResponse
from .models import Post

def home(request):
    #return HttpResponse("Bienvenido a Django")
    posts = Post.objects.all() # Obtenemos todos los posts
    return render(request, "blog/home.html", {'posts': posts}) # Enviamos los posts a la plantilla

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, "blog/post.html", {'post': post}) 