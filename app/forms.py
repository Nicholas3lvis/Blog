from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from . models import CustomUser

class RegisterForms(UserCreationForm):
    class Meta:
        model = get_user_model()
        # fields = '__all__'
        fields=['username','email','last_name',"first_name",'password1','password2','profile_pic']
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Your Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your User Name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Your Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Last Name'}))
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control', 'placeholder':'Enter Your Last Name'}))
    


class EditProfile(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields=['last_name',"first_name",'username','phone','address','residence','social_link','core_skill','profile_pic', 'bio']
        
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Phone Number'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your UserName'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Adress'}))
    residence = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Confirm Residence'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Last Name'}))
    # updated = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'Enter Date'}))
    # freelance = forms.ModelChoiceField(queryset=CustomUser.objects.filter(),widget=forms.Select(attrs={'class':'form-control', 'placeholder':'Enter Your Last Name'}))
    social_link = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Social Link'}))
    core_skill = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Core Skill'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Your BIO'}))
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control', 'placeholder':'Enter Your Last Name'}))



class SubscriptionForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))