import requests
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import SubscriptionForm

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            api_key = settings.MAILCHIMP_API_KEY
            audience_id = settings.MAILCHIMP_AUDIENCE_ID
            
            try:
                data_center = api_key.split('-')[1]
            except IndexError:
                return redirect('subscription:failure')
            
            url = f'https://{data_center}.api.mailchimp.com/3.0/lists/{audience_id}/members'
            data = {
                'email_address': email,
                'status': 'subscribed',
            }
            headers = {
                'Authorization': f'Bearer {api_key}'
            }
            response = requests.post(url, json=data, headers=headers)
            
            if response.status_code == 200:
                return redirect('subscription:success')
            elif response.status_code == 400 and response.json().get('title') == 'Member Exists':
                return redirect('subscription:duplicate')
            else:
                return redirect('subscription:failure')

    return redirect('/')
    

def success(request):
    return render(request, 'subscription/success.html')

def failure(request):
    return render(request, 'subscription/failure.html')

def duplicate(request):
    return render(request, 'subscription/duplicate.html')