from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to Stefan Dodds Admin Page</h1>")
