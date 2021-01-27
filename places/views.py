from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Здесь будет карта</h1>")