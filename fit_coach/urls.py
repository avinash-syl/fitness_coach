from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("progress/", views.in_progress, name="progress"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("detail/<int:course_id>/", views.course_detail, name="detail"),
    path("start/", views.start_course, name="start"),
    path("terminate/", views.terminate_course, name="terminate"),
    path("questionnaire/", views.questionnaire, name="questionnaire")
]
