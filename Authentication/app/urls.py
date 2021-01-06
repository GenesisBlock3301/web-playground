from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register-user'),
    path('login/', views.LoginView.as_view(), name='login-user'),
    path('logout/', views.user_logout, name='logout-user'),
    path('', views.HomeView.as_view(), name='home'),
]
