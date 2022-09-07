from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import NewUserForm,ProfileForm
from .models import Profile
from main.utils import profile_uploader
 
# Create your views here.
def index_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        pswd = request.POST['password']
        try:
            user = authenticate(request, username = username, password = pswd)
            login(request, user)
            return redirect('/chats')
        except:
            return HttpResponse('Failed to login')
        
    return render(request, 'login.html', {})

def signup_view(request):
    form = NewUserForm(request.POST, request.FILES)
    if form.is_valid():
        user = form.save()
        return redirect(f'/accounts/profile/{user.id}')
    
    context = {
        'form': form
    }
    
    return render(request, 'signin.html', context)


def setup_view(request, user):
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
        activated_user = User.objects.get(id = user)
        profile_name = profile_uploader(activated_user, request.FILES['profile_image'])
        newProfile = Profile(user = activated_user, profile_image_url = profile_name)
        newProfile.save()
        return redirect('/')
    
    context = {
        'form': form
    }
    
    return render(request, 'setup.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')