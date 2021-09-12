from django import forms
from . import models


class BasicDetailsForm(forms.ModelForm):
    # class to store all the model form fields from models.py
    class Meta:
        model = models.BasicDetails
        fields = ["name", "sex", "annual_income", "email", "mobile", "occupation", "DOB"]


class PresentLocationForm(forms.ModelForm):
    class Meta:
        model = models.PresentLocation
        fields = ["country", "state", "city", "street", "pincode"]


class MoneyTransferForm(forms.ModelForm):
    class Meta:
        model = models.MoneyTransfer
        fields = [
            "enter_your_user_name",
            "enter_the_destination_account_number",
            "enter_the_amount_to_be_transferred_in_INR"
        ]

class Loan(forms.ModelForm):
    class Meta:
        model=models.Loan
        fields = [
            "enter_your_user_name",
            "enter_the_your_account_number",
            "enter_the_amount_to_be_transferred_in_INR"
        ]
