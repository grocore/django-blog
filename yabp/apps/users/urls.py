from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.user_profile, name='user-profile'),
    path('register/', views.user_create, name='user-create'),
    path('profile/', views.user_profile, name='user-profile'),
    path('login/', auth_views.LoginView.as_view(template_name='user_login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user_logout.html'), name='user-logout'),
]
