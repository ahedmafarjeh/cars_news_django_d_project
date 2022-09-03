from django import forms
from .models import Piece,posts
class NewPieceForm(forms.ModelForm):

     class Meta:
        model = Piece
        fields = ['piece_name','price','is_available']
class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = posts
        fields = ['message']