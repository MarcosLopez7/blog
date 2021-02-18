from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola mundo! estàs entrando en los blogs")