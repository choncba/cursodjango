from django.shortcuts import render, HttpResponse

def home(request):
    #return HttpResponse("Bienvenido a Django")
    return render(request, "blog/home.html")