from django.shortcuts import render
from ..service import util
from ..service.mock_service import MockDataService

mockService = MockDataService()


def homepage(request):
    user = request.user
    if user is not None:
        # course data should be fetched from database, now just mocking
        courses = mockService.getWorkOutRecommendation(user.username)
        user.username = util.getUsernameFromEmailAddr(user.username)

    return render(request, 'index.html', {'user': user, 'courses': courses})


class user_details():
    pass
