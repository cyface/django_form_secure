"""
Forms
"""
from django.forms import ModelForm, HiddenInput

from project.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message', 'message_creator', 'trip']
        widgets = {
            'message_creator': HiddenInput(),
            'trip': HiddenInput(),
        }
