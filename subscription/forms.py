from django import forms

class SubscriptionForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email address',
        'class': 'form-control',
    }))
