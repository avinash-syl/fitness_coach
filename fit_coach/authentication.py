from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def login(request):
    username = request['username']
    password = request['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request=request, user=user)
    else:
        return HttpResponse("Invalid credentials", status=400)
    
def register(request):
    username = request['username']
    password = request['password']
    
    user = User.objects.create(username=username, email=None, password=password)