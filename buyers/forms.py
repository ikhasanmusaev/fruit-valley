from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from buyers.models import User


class SignupForm(UserCreationForm):
    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    username = forms.EmailInput()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    username = forms.EmailInput(attrs={'placeholder': 'Email'})
    password = forms.PasswordInput(attrs={'placeholder': '*********'})
