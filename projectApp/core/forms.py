from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Sign up form for new users
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


# Creating new projects
class CreateListForm(forms.Form):
    name = forms.CharField(label="Name ", max_length=300)


class DateForm(forms.Form):
    todo = forms.CharField(
    widget=forms.TextInput(attrs={"class":"form-control"}))
    date_1=forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker'}))
