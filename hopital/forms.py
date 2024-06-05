# forms.py
from django import forms
from .models import Prescription

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['title']  # supposer que vous avez uniquement besoin du titre pour créer une nouvelle prescription


