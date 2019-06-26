from django import forms
from .models import cinemareview

class PostForm(forms.ModelForm):
    class Meta:
        model = cinemareview
        fields = ('nickname','rate','review',)