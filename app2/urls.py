from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('singlepage/<slug:slug>', views.singlepage, name='singlepage'),
    path('create_post/', views.create_post, name='create_post'),
    path('update_post/<slug:slug>', views.update_post, name='update_post'),
    path('delete_post/<slug:slug>', views.delete_post, name='delete_post'),
]
