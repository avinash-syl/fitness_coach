from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from fit_coach.service.mock_service import MockDataService

mockService = MockDataService()


@login_required
def course_detail(request, course_id):
    # here should query for the course detail by id from database
    detail = mockService.getCourseDetailById(course_id)
    return render(request, 'course_detail.html', {"detail": detail})


@login_required
def start_course(request):
    user = request.user
    courseId = request.POST.get('course_id')

    # backend should implement the logic of adding course into in progress

    return JsonResponse({})


@login_required
def terminate_course(request):
    user = request.user
    # backend should implement the logic of removing course from in progress

    return JsonResponse({})


def in_progress(request):
    user = request.user
    course = None
    if user is not None:
        # course data should be fetched from database with respect to different users, now just mocking
        courses = mockService.getInProgressCourses(user.username)
    return render(request, 'in_progress.html', {'courses': courses})
