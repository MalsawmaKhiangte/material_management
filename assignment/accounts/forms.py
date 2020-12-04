from django import forms
from django.contrib.auth.models import User
from .models import Profile

DISTRICT_CHOICE = [
    ('' , '--------') ,('Purchase Manager' , 'Purchase Manager') , ('District Manager' , 'District Manager')
]
CITY_CHOICE =[
    ('' , '--------') , ('Aizawl' , 'Aizawl') ,('Lunglei' , 'Lunglei')
]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    designation = forms.ChoiceField(choices=DISTRICT_CHOICE)
    city = forms.ChoiceField(choices=CITY_CHOICE)
    password = forms.CharField(label= 'Password' , widget = forms.PasswordInput)
    password2 = forms.CharField(label= 'Confrim_Password' , widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password dont match')
        return cd['password2']
