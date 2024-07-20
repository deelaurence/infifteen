from django import forms
from django.contrib.auth.models import User
from .models import *

class QuestionForm(forms.ModelForm):
    print('calling question form')
    question_text = forms.CharField(required=True)
    optionA = forms.CharField(required=True)
    optionB = forms.CharField(required=True)
    optionC = forms.CharField(required=False)  # Explicitly set required to False
    optionD = forms.CharField(required=False) 
    category = forms.CharField(required=True) 
    answer = forms.CharField(required=True)


    class Meta:
        model = Question
        fields = ('question_text','optionA','optionB','optionC','optionD','category','answer')

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError('This email is already in use.')
    #     return email


    # def clean_password2(self):
        
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords do not match")
    #     return password2

    # def save(self, commit=True):
    #     print('tryna save signup form')
    #     user = super(SignupForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     user.name = self.cleaned_data['name']
    #     user.password = make_password(self.cleaned_data['password1'])
    #     if commit:
    #         user.save()
    #     return user



