from django import forms, http
from django.contrib.auth.models import User
from PhotoApp.models import Photo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class PhotoForm(forms.ModelForm):
    class Meta():
        model = Photo
        fields = ('title','image','captions','saveAsDraft')

    