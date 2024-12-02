from django import forms
from .models import ContactMessage, GalleryImage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['email', 'message']

class GalleryForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['user_email', 'image']
