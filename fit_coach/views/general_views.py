from django.shortcuts import render
from ..service.auth_service import AuthService

authService = AuthService()


def homepage(request):
    user = request.user
    if user is not None:
        user.username = authService.getUsernameFromEmailAddr(emailAddr=user.username)
    return render(request, 'index.html', {'user': user})


def in_progress(request):
    return render(request, 'in_progress.html')


class user_details():
    pass
