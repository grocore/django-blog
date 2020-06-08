from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.user_profile, name='user-profile'),
    path('signup/', views.user_create, name='user-create'),
]
