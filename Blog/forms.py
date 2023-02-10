from django import forms
from .models import Commentaire

class CommentaireForm(forms.ModelForm, forms.Form):
    nom = forms.CharField(
        label="Your name", required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        label="Your Email Address", required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    commantaire = forms.CharField(
        label="Commentaire", required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows':3}))
    class Meta:
        model = Commentaire
        fields = ['nom', 'email', 'commantaire']