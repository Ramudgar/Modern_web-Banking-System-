from profiles import models
from django import forms

class BasicDetailsForm(forms.ModelForm):
    # class to store all the model form fields from models.py
    class Meta:
        model = models.BasicDetails
        fields= ['name','sex','email','mobile','occupation','DOB']
        