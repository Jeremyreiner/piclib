from django.urls import path
from . import views 

urlpatterns = [
    path('photos/add/', views.AddImage, name='add'),
    path('post/<int:pk>/update/', views.PhotoUpdateView.as_view(), name='update_photo'),
    path('photos/<int:pk>/', views.SinglePhoto, name='view_photo'),
    path('photos/<int:pk>/delete/', views.PhotoDeleteView.as_view(), name='delete_photo'),
    path('photos/category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='delete_category'),
    path('photos/<int:photo_id>/comment/', views.CommentCreateView.as_view(), name='new_comment'),
    path('about/us/', views.about, name='about'),
    path('', views.gallery, name='gallery'),
]
