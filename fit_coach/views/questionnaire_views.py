from django.shortcuts import render, redirect
from ..forms import QuestionnaireForm
from django.contrib.auth.decorators import login_required
from .model_operations import update_user_questionnaire
from django.db import IntegrityError

@login_required
def questionnaire(request):
    user = request.user
    print(user, flush=True)
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            try:
                update_user_questionnaire(form.full_clean(), user.username)
            except IntegrityError as e:
                form = QuestionnaireForm()
                form.add_error(None, "Error while updating user, try again")
                return render(request, 'questionnaire.html', {'form': form})
            return redirect('home')
        else:
            form = QuestionnaireForm()
    else:
        form = QuestionnaireForm()
    return render(request, 'questionnaire.html', {'form': form})
