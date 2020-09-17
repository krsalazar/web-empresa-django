from .models import Link

def dic_context(request):
    contexto = {}
    links = Link.objects.all()
    for link in links:
        contexto[link.key] = link.url
    return contexto