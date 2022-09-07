from django.shortcuts import render, HttpResponse, redirect
from accounts.models import Profile
from django.contrib.auth.models import User
from .models import Chat, Message, Notification, MyChat
from django.http import JsonResponse
from .utils import image_uploader, video_uploader 
from .forms import ImageForm, VideoForm

def create_chat(request, profile):
    #get user
    user = User.objects.get(id=request.user.id)
    #get profiles
    active_profile = Profile.objects.get(id = profile)
    userProfile = Profile.objects.get(user = user)
    
    #try existance of chat
    try:
        exist = Chat.objects.get(first_user = userProfile, last_user = active_profile)
        return redirect(f'/main/message/{exist.id}')
    except:    
        try:
            exist = Chat.objects.get(first_user = active_profile, last_user = userProfile)
            return redirect(f'/main/message/{exist.id}')
        except:
            #create chat object
            newChat = Chat(first_user = userProfile, last_user = active_profile)
            newChat.save()
            return redirect(f'/main/message/{newChat.id}')
        
    return redirect('/chats') 


def chats_view(request):
    #get current user profile
    user = User.objects.get(id=request.user.id)
    userProfile = Profile.objects.get(user = user)
    #collect user chats from working user profile
    chatlist = Chat.objects.filter(first_user = userProfile.id)
    chatlist = chatlist.union(Chat.objects.filter(last_user = userProfile.id))
    context = {
        'chatlist':chatlist,
        'myProfile': userProfile
    }
    
    return render(request, 'chats.html', context)

def globe_view(request):
    user = User.objects.get(id=request.user.id)
    userProfile = Profile.objects.get(user = user)
    globe = Profile.objects.all()
    context = {
        'globe': globe,
        'myProfile': userProfile
    }
    return render(request, 'globe.html', context)

def profile_view(request):
    user = User.objects.get(id=request.user.id)
    userProfile = Profile.objects.get(user = user)
    context = {
        'myProfile': userProfile
    }
    return render(request, 'profile.html', context)
    
def message_view(request, chat_id):
    # get chat
    chat = Chat.objects.get(id = chat_id)
    # collect messages
    messages = Message.objects.filter(chat_id = chat)
    myProfile = Profile.objects.get(user= request.user)
    
    sendImage(request, chat_id)
    
    context = {
        'active_chat':chat,
        'messages': messages,
        'myProfile': myProfile,
    }
    
    return render(request, 'playground.html', context)


def get_messages(request, chat_id):
    # get chat
    chat = Chat.objects.get(id = chat_id)
    messages = Message.objects.filter(chat_id = chat)
    
    return JsonResponse({'messages': list(messages.values())})


def sendText(request, chat_id):
    user = User.objects.get(id=request.user.id)
    userProfile = Profile.objects.get(user = user)
    # get chat
    chat = Chat.objects.get(id = chat_id)
    #get form data
    if request.POST:
        msg = request.POST['content']
        newMessage = Message(chat_id = chat, sender = userProfile, content = msg, text = True)
        newMessage.save()
        
    return HttpResponse('send..')


def deleteMessage(request, msgId):
    # get message
    msg = Message.objects.get(id = msgId)
    msg_path = msg.chat_id.id
    msg.delete()
    return redirect(f'/main/message/{msg_path}')

def sendImage(request, chat_id):
    # get chat
    chat = Chat.objects.get(id = chat_id)
    user = User.objects.get(id=request.user.id)
    userProfile = Profile.objects.get(user = user)
    imageForm = ImageForm(request.POST or request.FILES)
    
    context = {
        'myProfile' : userProfile,
        'active_chat': chat,
        'iForm': imageForm 
    }
    if request.POST or request.FILES:
        file = request.FILES['image']
        file_url = image_uploader(file)
        newMessage = Message(chat_id = chat, sender = userProfile, content = file_url, text = False, image = True)
        newMessage.save()
        return redirect(f'/main/message/{chat.id}')
        
    return render(request, 'share_image.html', context)
        

       
def sendVideo(request, chat_id):
    # get chat
    chat = Chat.objects.get(id = chat_id)
    user = User.objects.get(id=request.user.id)
    userProfile = Profile.objects.get(user = user)
    videoForm = VideoForm(request.POST or request.FILES)
    
    context = {
        'myProfile' : userProfile,
        'active_chat': chat,
        'vForm': videoForm 
    }
    if request.POST or request.FILES:
        file = request.FILES['video']
        file_url = video_uploader(file)
        newMessage = Message(chat_id = chat, sender = userProfile, content = file_url, text = False, video = True)
        newMessage.save()
        return redirect(f'/main/message/{chat.id}')
        
    return render(request, 'share_video.html', context) 