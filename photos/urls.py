from django.urls import path
from . import views 

urlpatterns = [
    path('add/', views.AddImage, name='add'),
    path('photo/<str:pk>/', views.SinglePhoto, name='view_photo'),
    path('', views.gallery, name='gallery'),
]
