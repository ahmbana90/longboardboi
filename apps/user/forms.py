from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Your username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Your email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Set Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})
