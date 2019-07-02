from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from bugtracker.models import Bug
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    status_choices= (
        ('Testers', 'Testers'),
        ('Programmers', 'Programmers')
    )
    email = forms.EmailField()
    status = forms.ChoiceField(choices=status_choices)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'status']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class BugRegisterForm(ModelForm):
    status_choices = (
        ('resolved', 'resolved'),
        ('unresolved', 'unresolved')
    )

    title = forms.CharField(max_length=255)
    description = forms.TextInput()

    class Meta:
        model = Bug
        fields = ['title', 'description']
