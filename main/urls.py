from django.urls import path
from . import views


urlpatterns = [
    path('', views.globe_view),
    path('chat/<int:profile>', views.create_chat, name='new_chat'),
    path('message/<int:chat_id>', views.message_view, name = 'playground'),
    path('collect/<int:chat_id>', views.get_messages, name='get_messages'),
    path('send/<int:chat_id>', views.sendText, name = 'send'),
    path('send_image/<int:chat_id>', views.sendImage, name = 'send_image'),
    path('send_video/<int:chat_id>', views.sendVideo, name = 'send_video'),
    path('del/<int:msgId>', views.deleteMessage)
]
