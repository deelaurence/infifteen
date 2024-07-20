from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.hashers import make_password


class SignupForm(forms.ModelForm):
    print('calling signup form')
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=255, required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}), required=True)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}), required=True)

    class Meta:
        model = User
        fields = ('email', 'name', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use.')
        return email


    def clean_password2(self):
        
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        print('tryna save signup form')
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['name']
        user.password = make_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user



class LoginForm(forms.ModelForm):
    print('calling login form')
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}), required=True)

    
    class Meta:
        model = User
        fields = ('email','password1')
    

    

    

