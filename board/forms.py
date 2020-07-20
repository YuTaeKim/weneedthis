from django import forms
from .models import User,Idea,Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class IdeaForm(forms.ModelForm):
    class Meta:
        model=Idea
        fields=['title','article']
        widgets={
            'article': forms.CharField(widget=CKEditorUploadingWidget()),
        }