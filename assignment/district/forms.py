from django import forms
from .models import quote , Aizawl , Lunglei

class quoteForm(forms.ModelForm):
    class Meta:
        model = quote
        fields = '__all__'
        exclude = [ 'created']

class reqForm(forms.Form):
    to_district = forms.CharField(max_length=50)
    req_material = forms.CharField(max_length=80)
    message = forms.CharField( widget=forms.Textarea )

class AdisChoices(forms.ModelForm):
    class Meta:
        model = Aizawl
        fields = ['send_to']

class LdisChoices(forms.ModelForm):
    class Meta:
        model = Lunglei
        fields = ['send_to']
