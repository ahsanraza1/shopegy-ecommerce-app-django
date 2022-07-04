from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, WoztiUser

class RegistrationForm ( UserCreationForm ):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'E-mail address'}))
    class Meta:
        model = WoztiUser
        fields = ('email', 'name', 'password1', 'password2')


class LoginForm(forms.Form):
    email = forms.EmailField(label="email", max_length=150)
    password = forms.CharField(label="Password", max_length=150, widget=forms.PasswordInput)

class Add_Product( forms.ModelForm ):
    class Meta:
        model = Product
        fields = '__all__'