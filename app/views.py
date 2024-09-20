from django.shortcuts import render,redirect,get_object_or_404,redirect
from . forms import RegisterForms, EditProfile, SubscriptionForm
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from app2.models import Blog

# Create your views here.

def signup(request):
    form = RegisterForms()
    if request.method == 'POST':
        form = RegisterForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Account created Successfully')
            return redirect('signup')
    context = {'form':form}
    return render(request, 'app/signup.html', context)


def signin(requst):
    if requst.method=='POST':
        email = requst.POST['email']
        password = requst.POST['password']
        
        user = authenticate(requst, email=email, password=password)
        if user is not None:
            login(requst, user)
            return redirect('home')
        else:
            messages.warning(requst, 'Invalid credentials')
            return redirect('signin')
    return render(requst, 'app/login.html')

def signout(requst):
    logout(requst)
    return redirect('home')

def profile(request):
    user = request.user
    blogs = Blog.objects.filter(user=user)
    return render(request, 'app/profile.html',{'user':user,'blogs':blogs})

@login_required(login_url='signin')
def edit_profile(request):
    if request.user.is_authenticated:
        user = request.user
        form =EditProfile(instance=user)
        if request.method=="POST":
            form = EditProfile(request.POST, request.FILES,instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile Updateded Successfuly')
                return redirect('profile')
    return render(request, 'app/edit_profile.html',{'form':form})





def users(request):
    users = CustomUser.objects.all()
    return render(request, 'app/users.html', {'users': users})

def user_profile(request, id):
    user = get_object_or_404(CustomUser, id=id) 
    use = CustomUser.objects.all()
    blogs = Blog.objects.filter(user=user)
    return render(request, 'app/user_profile.html', {'user': user, 'blogs':blogs,'use':use})

def kindly(request):
    return render (request,'app/kindly.html') 


