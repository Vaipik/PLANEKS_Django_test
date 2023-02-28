from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .libs import constants


User = get_user_model()


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        min_length=constants.USER_MIN_LEGNTH,
        max_length=constants.USER_MAX_LEGNTH,
        label="Enter username",
        widget=forms.TextInput(attrs={
            "class": "form-control mt-3",
            "placeholder": "username"
        })
    )
    password1 = forms.CharField(
        max_length=constants.PASSWORD_MAX_LENGTH,
        label="Enter your password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control mt-3",
            "placeholder": "Enter password"
        })
    )
    password2 = forms.CharField(
        min_length=constants.PASSWORD_MIN_LENGTH,
        max_length=constants.PASSWORD_MAX_LENGTH,
        label="Repeat your password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control mt-3",
            "placeholder": "Repeat password"
        })
    )

    class Meta:
        model = User
        fields = ["username"]


class SignInForm(AuthenticationForm):
    username = forms.CharField(
        min_length=constants.USER_MIN_LEGNTH,
        max_length=constants.USER_MAX_LEGNTH,
        label="Enter username",
        widget=forms.TextInput(attrs={
            "class": "form-control mt-3",
            "placeholder": "username",  # required to prettify view of modal form
        })
    )
    password = forms.CharField(
        min_length=constants.PASSWORD_MIN_LENGTH,
        max_length=constants.PASSWORD_MAX_LENGTH,
        label="Enter password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control mt-3",
            "placeholder": "password",  # required to prettify view of modal form
        })
    )
