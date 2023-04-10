from django.http import JsonResponse
from fit_coach/models.py import User

def get_users(request):
    users = User.objects.all().values()
    users_list = list(users)
    return JsonResponse(users_list, safe=False)