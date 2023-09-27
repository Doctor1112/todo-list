from django.forms import modelformset_factory
from .models import Todo
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.widgets import TextInput
from django.contrib.auth.forms import AuthenticationForm

from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("title", )
    title = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 2, 'cols': 50}))

class DescriptionForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['description']
        widgets = {"description": forms.Textarea(attrs={'rows': 4, 'cols': 50})}
        labels = {"description": ""}
        required = {"description": False}

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")

class UserForm(ModelForm):
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль',
                               widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("username", "email")
        labels = {
            'username': 'Имя пользователя',
            "email": "email"
        }

    def clean_password2(self):
        if self.cleaned_data["password"] != self.cleaned_data["password2"]:
            raise forms.ValidationError("Пароли не совпадают")
        return self.cleaned_data["password2"]

    def save(self):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data['password'])
        user.save()
        return user



