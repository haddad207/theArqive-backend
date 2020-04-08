from django import forms
from .models import pin

class PostForm(forms.ModelForm):
    class Meta:
        model = pin
        fields = [
            'title',
            'description',
            'tags',
        ]