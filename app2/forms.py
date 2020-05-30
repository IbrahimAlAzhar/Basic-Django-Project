from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput) # creating password explicitly which is not present in user

    class Meta:
        model = User # using User model which is build in database
        fields = ['username','email','password'] # override these attributes from user model
