from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("Inicio")
    return render(request, 'core/home.html')

def about(request):
    #return HttpResponse("Acerca de")
    return render(request, 'core/about.html')

def services(request):
    #return HttpResponse("Servicios")
    return render(request, 'core/services.html')

def store(request):
    #return HttpResponse("Tienda")
    return render(request, 'core/store.html')
