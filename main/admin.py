from django.contrib import admin
from .models import Chat, Notification, Message

# Register your models here.

# chat
class ChatAdmin(admin.ModelAdmin):
    list_display = ('first_user', 'last_user')
admin.site.register(Chat, ChatAdmin)

# notifications
class NotificationAdmin(admin.ModelAdmin):
    list_disply = ('notification_from','notification_to','content')
admin.site.register(Notification, NotificationAdmin)

# message admin
class MessageAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'time_sent')
    
admin.site.register(Message, MessageAdmin)