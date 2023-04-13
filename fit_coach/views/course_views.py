from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.db import IntegrityError

from .model_operations import *
from fit_coach.service.mock_service import MockDataService

mockService = MockDataService()


@login_required
def course_detail(request, course_id):
    # here should query for the course detail by id from database
    workout_plan = get_workout_plan(course_id)
    return render(request, 'course_detail.html', {"detail": workout_plan})


@login_required
def start_course(request):
    user = request.user
    course_id = request.POST.get('course_id')
    try:
        update_current_plan(user.username, course_id)
    except IntegrityError as e:
        return HttpResponseRedirect(request.path_info)
    return JsonResponse({})


@login_required
def terminate_course(request, course_id):
    user = request.user
    
    return redirect('detail', course_id)

@login_required
def feedback(request, course_id):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        update_user_rating(request.user.username, rating=rating)
        return redirect('terminate', course_id)
    else:
        return redirect('detail', course_id)

@login_required
def in_progress(request):
    user = request.user
    if request.user.is_authenticated():
        courses = get_user_active_plans(user.username)
    return render(request, 'in_progress.html', {'courses': courses})
