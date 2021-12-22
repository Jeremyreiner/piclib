from django.urls import path
from . import views 

urlpatterns = [
    path('photos/add/', views.AddImage, name='add'),
    path('photos/<str:pk>/', views.SinglePhoto, name='view_photo'),
    path('photos/<int:photo_id>/comment/', views.CommentCreateView.as_view(), name='new_comment'),
    path('about/us/', views.about, name='about'),
    path('', views.gallery, name='gallery'),
]
