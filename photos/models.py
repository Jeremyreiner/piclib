from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length= 100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True, related_name='user_profile') 
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description= models.TextField(null=False, blank=False)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.description


class Comment(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, null=False, blank=True, related_name='comments')
    content = models.CharField(max_length=350)
    timestamp = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('view_photo', kwargs={'pk': self.photo.id})

    def __str__(self):
        return f"Comment by {self.owner} on {self.photo}."
