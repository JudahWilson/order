from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm, PasswordChangeForm,
    UserChangeForm, PasswordResetForm, SetPasswordForm,
    AdminPasswordChangeForm
)  
from django.contrib.auth import get_user_model, authenticate, login, logout




'''
Default Authentication Forms
'''    
class _UserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2')

class _AuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class _PasswordChangeForm(PasswordChangeForm):
    pass


class _UserChangeForm(UserChangeForm):
    pass


class _PasswordResetForm(PasswordResetForm):
    pass


class _SetPasswordForm(SetPasswordForm):
    pass


class _AdminPasswordChangeForm(AdminPasswordChangeForm):
    pass