from django.urls import path
from . import views

app_name = 'subscription'

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('success/', views.success, name='success'),
    path('failure/', views.failure, name='failure'),
    path('duplicate/', views.duplicate, name='duplicate'),
]
