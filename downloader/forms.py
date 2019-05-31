from django import forms
from .models import Link

class LinkForm(forms.Form):
    url = forms.URLField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter url video from youtube.com'
    }))

    class Meta:
        model = Link
        fields = [
            'url'
        ]

