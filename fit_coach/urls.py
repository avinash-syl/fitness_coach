from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("progress/", views.in_progress, name="progress"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout")
]
