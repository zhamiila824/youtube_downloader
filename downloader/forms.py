from django import forms
from .models import Request


class LinkForm(forms.Form):
    url = forms.RegexField(regex=r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$')

    class Meta:
        model = Request
        fields = [
            'url'
        ]

