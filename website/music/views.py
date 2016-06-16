from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>My First Django App</h1>")