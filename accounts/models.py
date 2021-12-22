from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model): 
    user= models.OneToOneField(User, on_delete= models.CASCADE)
    first_name=models.CharField(max_length= 50, blank=True, null=True)
    last_name=models.CharField(max_length= 50, blank=True, null=True)
    full_name= models.CharField(max_length= 50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image= models.ImageField(default= 'default.jpg', upload_to='media/profile_pics')
    phone= models.CharField(max_length= 12)
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)