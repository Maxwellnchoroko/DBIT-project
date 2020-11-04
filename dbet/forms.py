from django import forms
from .models import Client,Player

class ClientForm(forms.ModelForm):
    class Meta:
        model= Client
        fields='__all__'

class PlayerForm(forms.ModelForm):
    class Meta:
        model= Player
        fields='__all__'