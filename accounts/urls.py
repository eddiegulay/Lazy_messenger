from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signup_view, name = 'signup'),
    path('profile/<int:user>', views.setup_view, name='setup'),
    path('logout/', views.logout_view, name = 'logout')
]
