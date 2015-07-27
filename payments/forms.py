from django import forms


class StripeForm(forms.Form):
    stripeToken = forms.CharField()
