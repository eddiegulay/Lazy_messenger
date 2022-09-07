from django.db import models
from accounts.models import Profile
# Create your models here.


class Chat(models.Model):
    first_user = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name = "first_user")
    last_user = models.ForeignKey(Profile, on_delete= models.CASCADE)

    def __str__(self):
        return self.last_user.user.username

class Notification(models.Model):
    notification_from =  models.ForeignKey(Profile, on_delete= models.CASCADE, related_name="contact_owner")
    notification_to =  models.ForeignKey(Profile, on_delete= models.CASCADE, )
    content = models.CharField(max_length = 100)
    
    
class Message(models.Model):
    chat_id = models.ForeignKey(Chat, on_delete= models.CASCADE)
    sender = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name='sender_host')
    content = models.CharField(max_length = 5000)
    time_sent = models.DateField(auto_now = True)
    text = models.BooleanField(default = True)
    image = models.BooleanField(default = False)
    video = models.BooleanField(default = False)
    
    
class MyChat(models.Model):
    chat = models.ForeignKey(Chat, on_delete = models.CASCADE)
    host = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name = 'host')