from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.Form):
    name = forms.CharField(label="Name" , max_length=100,required=True)
    email = forms.EmailField(label="Email",required=True)
    message = forms.CharField(label="Message",required=True)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']