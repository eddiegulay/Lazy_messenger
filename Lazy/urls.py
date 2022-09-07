"""Lazy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from accounts.views import index_view
from main.views import chats_view, globe_view, profile_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name = 'login'),
    path('accounts/',include('accounts.urls')),
    path('main/', include('main.urls')),
    path('chats/', chats_view, name = 'chats'),
    path('globe/', globe_view, name = 'globe'),
    path('profile/', profile_view, name = 'profile')
]
