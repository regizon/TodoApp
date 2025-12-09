from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    username = forms.CharField(label='', max_length=30, min_length=3, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                                            'placeholder': 'Username',
                                                                                                            'id': 'exampleInputEmail1'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'exampleInputPassword1',
        'placeholder': 'Password',
    }), min_length=3)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username already exists')
        return username


class LoginForm(forms.Form):
    username = forms.CharField(label='', max_length=30, min_length=3,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Username',
                                                             'id': 'exampleInputEmail1'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'exampleInputPassword1',
        'placeholder': 'Password',
    }), min_length=3)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists() is not True:
            raise ValidationError('User was not found')
        return username


class AddTaskForm(forms.Form):
    title = forms.CharField(label='', max_length=30, min_length=5, widget=forms.TextInput(attrs={'placeholder': 'Task title'}))

class SearchForm(forms.Form):
    title = forms.CharField(label='', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Search', 'class': 'form-control me-2 mt-3', 'type': 'search', 'aria-label':'Search'}))