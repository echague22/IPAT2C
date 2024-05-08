from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout')
]