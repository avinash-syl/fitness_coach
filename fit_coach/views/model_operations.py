from ..models import FitUser, WorkoutPlan

def update_user_questionnaire(form_data, username):
    fit_user = FitUser.objects.get(username=username)
    fit_user.age = form_data['age']
    fit_user.gender = form_data['gender']
    fit_user.interest = form_data['interest']
    fit_user.fitness_goal = form_data['fitness_goal']
    
    fit_user.save()
    
def update_user_rating(rating, username):
    fit_user = FitUser.objects.get(username=username)
    fit_user.rating = rating
    
    fit_user.save()

def get_workout_plan(id):
    workout_plan = WorkoutPlan.objects.get(id = id)
    return workout_plan

def update_current_plan(id):
    pass

def terminate_user_plan(username, course_id):
    fit_user = FitUser.objects.get(username=username)
    current_plan_ids = fit_user.profile.current_plans
    
    
def get_user_active_plans(username):
    fit_user = FitUser.objects.get(username=username)
    current_plan_ids = fit_user.profile.current_plans
    plans = WorkoutPlan.objects.filter(id__in=current_plan_ids)
    return plans
