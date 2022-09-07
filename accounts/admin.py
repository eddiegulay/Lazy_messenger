from django.contrib import admin
from .models import Profile

# user profile
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_image_url')
    
admin.site.register(Profile, ProfileAdmin)
