from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def default_profile():
    return 'img/logo.png'

def upload_image_to(self):
    return f'profile_uploads/{self.username}/{"profile.png"}'

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    profile_image_url = models.CharField(default = default_profile, blank = True, null = True, max_length = 555550)
    profile_image = models.ImageField(blank = True)
    
    
    def __str__(self):
        return self.user.username
    