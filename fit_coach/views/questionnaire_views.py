from django.shortcuts import render, redirect
from ..forms import QuestionnaireForm
from django.contrib.auth.decorators import login_required
from .model_operations import update_user_questionnaire
import logging

@login_required
def questionnaire(request):
    user = request.user
    print(user, flush=True)
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            cleaned_data = form.clean()
            print(cleaned_data, flush=True)
            logging.info(form)
            try:
                update_user_questionnaire(cleaned_data, user.username)
                return redirect('home')
            except:
                form.add_error(None, "Error while updating user, try again")
                return render(request, 'questionnaire.html', {'form': form})
        else:
            return render(request, 'questionnaire.html', {'form': form})
    else:
        form = QuestionnaireForm()
    return render(request, 'questionnaire.html', {'form': form})
