from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model): 
    user= models.OneToOneField(User, on_delete= models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_image= models.ImageField(default='profile_pics\i.jpg', upload_to='profile_pics')
    phone= models.CharField(max_length= 12)
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)