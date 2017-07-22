from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Teacher, ParentalUnit
from django.db import models
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all(),empty_label=None,required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

# def teacher_list():
#     teachers = Teacher.objects.all()
#     return teachers
#
#
# class UserChooseForm(forms.Form):
#     choose_user = forms.ChoiceField(choices=user_list())
#
#
# class UserEditForm(forms.Form):
#     user_name = forms.CharField(label="Username")
#     password = forms.CharField(label="Password")
#     first_name = forms.CharField(label="First Name")
#     last_name = forms.CharField(label="Last Name", required=False)
#     email = forms.CharField(label="Email address")



