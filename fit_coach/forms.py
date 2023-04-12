import os.path

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from fitness_coach import settings


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

class QuestionnaireForm(forms.Form):
    gender = [('M', 'Male'), ('F', 'Female')]
    fitness_goal = [('WL', 'Weight Loss'),
                    ('MS', 'Muscle Strength'),
                    ('CA', 'Cardiovascular Endurance'),
                    ('FF', 'Flexibility and Balance'),
                    ]
    # interests
    interests_file = os.path.join(settings.BASE_DIR, 'data', 'interests.txt')
    with open(interests_file) as f:
        interest_choices = [(line.strip(), line.strip().capitalize()) for line in f]

    age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}))
    gender = forms.ChoiceField(choices=gender, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}), label='Gender')
    interest = forms.ChoiceField(choices=interest_choices, widget=forms.Select(attrs={'class': 'form-select'}), label='What are your interests?')
    fitness_goal = forms.MultipleChoiceField(choices=fitness_goal, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}), label='What is your fitness goal? (Select all that apply)')