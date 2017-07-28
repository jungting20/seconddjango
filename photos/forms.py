from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User

from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        #쉼표는 필수임
        fields = ('image', 'content',)

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ('username','email','password')




