from django import forms
from .models import panier
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth

class PanierForm(forms.ModelForm, forms.Form):
    auth = forms.CharField(
        label="username", required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    quantite = forms.IntegerField(
        label="quantite", required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows':3}))
    class Meta:
        model = panier
        fields = ['article','auth','quantite']
