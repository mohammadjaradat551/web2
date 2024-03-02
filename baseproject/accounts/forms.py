from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from property.models import Property


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


    
#UserCreationForm, which is a subclass of ModelForm3.
#The UserCreationForm creates a user
class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'phone_number', 'address']


class PasswordResetForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class AddListForm(forms.ModelForm):
    class Meta:
        model = Property
        fields= ['name', 'description', 'price', 'main_image','place', 'category']


