from django import forms
from .models import NewsTopic, posts
import datetime as date
class NewNewsForm(forms.ModelForm):
     class Meta:
         model = NewsTopic
         fields = ['description']
class CommentForm(forms.ModelForm):
    class Meta:
        model = posts
        fields = ['message']