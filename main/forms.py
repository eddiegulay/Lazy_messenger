from django import forms

class ImageForm(forms.Form):
    image = forms.ImageField(label = '', widget = forms.FileInput(attrs={'class':'file_select_input'}))
    
class VideoForm(forms.Form):
    video = forms.FileField(label = '', widget = forms.FileInput(attrs={'class':'file_select_input','accept':'video/*'}))