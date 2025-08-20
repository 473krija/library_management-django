from django import forms
from .models import Fine

class FineForm(forms.ModelForm):
    class Meta:
        model = Fine
        fields = ['amount', 'reason', 'paid']

