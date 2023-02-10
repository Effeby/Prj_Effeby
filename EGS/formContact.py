from django import forms
from .models import Contact

class ContactForm(forms.ModelForm, forms.Form):
    nom = forms.CharField(
        label="Your name", required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        label="Your Email Address", required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    suject = forms.CharField(
        label="suject", required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows':3}))
    text = forms.CharField(
        label="text", required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows':3}))
    class Meta:
        model = Contact
        fields = ['nom', 'email','suject', 'text']
