from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('profile/',views.profile, name='profile'),
    path('edit_profile/',views.edit_profile, name='edit_profile'),
    path('users/',views.users, name='users'),
    path('profile/<int:id>/', views.user_profile, name='user_profile'),
    path('kindly/', views.kindly, name='kindly'),
]
