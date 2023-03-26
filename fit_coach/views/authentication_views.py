from django.shortcuts import render

# Views for login and signup pages
class login_view():
    def login(request):
        return render(request, 'login.html')

    def signup(request):
        return render(request, 'signup.html')