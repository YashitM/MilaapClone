from django import forms


class FundForm(forms.Form):
    fund_amount = forms.IntegerField()
