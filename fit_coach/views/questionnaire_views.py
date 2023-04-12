from django.shortcuts import render, redirect
from ..forms import QuestionnaireForm
from django.contrib.auth.decorators import login_required


@login_required
def questionnaire(request):
    user = request.user

    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            interest = form.cleaned_data['interest']
            fitness_goal = form.cleaned_data['fitness_goal']
            '''
                write into database to initialize the user model
            '''
            return redirect('home')
        else:
            form = QuestionnaireForm()
    else:
        form = QuestionnaireForm()
    return render(request, 'questionnaire.html', {'form': form})
