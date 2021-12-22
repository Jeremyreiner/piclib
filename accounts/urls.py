from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'), 
    path('register/', views.registration, name='register'),
    path('logout/', views.logout, name='logout'),
    path('profile/<str:username>/', views.UserDetailView.as_view(), name='user_profile'),
    path('profile/edit/<str:username>/', views.ProfileUpdate, name='profile_edit'),
]
