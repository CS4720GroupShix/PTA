from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Teacher, ParentalUnit, Homework, WishlistItem
from django.db import models
from django.forms import ModelForm
from datetime import date

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all(),empty_label=None,required=True, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class AddHomeworkForm(ModelForm):
    # title = forms.CharField(max_length=50, required=True, help_text='Required.')
    # description = forms.CharField(required=True, help_text='Required.')
    # date_assigned = forms.DateField(required=True, default=date.today)
    # date_due = forms.DateField(required=False)
    # points = forms.DecimalField(required=False, max_digits=3, decimal_places=1)

    class Meta:
        model = Homework
        fields = ('title', 'description', 'date_assigned', 'due_date', 'points',)

class AddWishlistForm(ModelForm):
    class Meta:
        model = WishlistItem
        fields = ('id','description',)

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



