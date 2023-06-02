# from django import forms
from django.forms import ModelForm
from .models import Contact

'''
#creating form using Form class

class Contact(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100, required=True)
    your_email = forms.EmailField(label="Email" ,required=True)
    phone = forms.IntegerField(max_value=11, required=True)
    massage = forms.CharField(label='massage', max_length=200, required=True,widget=forms.Textarea)
'''


#creating forms using Model Forms..

class Contact_form(ModelForm):
    class Meta:
        model = Contact
        fields = [
            "your_name",
            "your_email",
            "phone",
            "massage",
        ]