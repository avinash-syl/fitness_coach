from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from ..forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from ..models import FitUser
import logging

# Views for login and signup pages
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print("test")
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User.objects.create(username=username)
            fit_user = FitUser.objects.create(username=username)
            fit_user.save()
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            login(request, user)
            # redirect to questionnaire
            return redirect(reverse('questionnaire'))
        return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
