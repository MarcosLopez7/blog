from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hola mundo! este es el index</h1>")