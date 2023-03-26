from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage_view.homepage, name="home"),
    path("progress/", views.in_progress_view.in_progress, name="progress"),
    path("login/", views.login_view.login, name="login"),
    path("signup/", views.login_view.signup, name="signup"),
]
