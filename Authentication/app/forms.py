from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import re


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                               required=True, max_length=30)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email ID'}),
                            required=True, max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                                required=True, max_length=30)
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}), required=True,
        max_length=30)

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("username already exists.")
        return username

    def clean_email(self):
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        email = self.cleaned_data['email']
        r = User.objects.filter(email=email)
        if r.count() or (email and not re.search(regex, email)):
            raise ValidationError("Your email used or incorrect.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password2 and password1 and password2 != password1:
            raise ValidationError("Password doesn't match.")
        return password2


class LoginForm(forms.Form):
    username = forms.CharField(label="",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                               required=True, max_length=30)
    password = forms.CharField(label="",
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                               required=True, max_length=30)


class UserEditForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}), required=True, max_length=30)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}), required=True, max_length=30)
    degree = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Qualifications'}), required=True, max_length=1000)

    description = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", 'placeholder': "Description"}))
    age = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Description"}))

