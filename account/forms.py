from django import forms
from .models import profile,Posts
from django.contrib.auth.models import User


class createpostform(forms.ModelForm):
    class Meta:
        model = Posts
        fields=[
        'author','title','body','post_img'
        ]

class createCustomUser(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields=[
        'username','email','password',
        ]
