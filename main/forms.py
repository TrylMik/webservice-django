from tkinter import Widget
from django import forms
from .models import *


class PostSpotForm(forms.ModelForm):
    class Meta:
        model = SpotsPost
        fields = ('title', 'author', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'','id':'user', 'type':'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'title':'Tytuł',
            'body': 'Treść',
        }

class CommentSpotForm(forms.ModelForm):
    class Meta:
        model = SpotsComment
        fields = ('author', 'body')
        
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'','id':'user', 'type':'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'body': 'Treść',
        }