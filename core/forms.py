from django import forms
from .models import Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-3 rounded bg-gray-900 border border-gray-700 text-white focus:border-blue-500 focus:outline-none',
                'placeholder': 'Your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full p-3 rounded bg-gray-900 border border-gray-700 text-white focus:border-blue-500 focus:outline-none',
                'placeholder': 'Your email address'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'w-full p-3 rounded bg-gray-900 border border-gray-700 text-white focus:border-blue-500 focus:outline-none',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full p-3 rounded bg-gray-900 border border-gray-700 text-white focus:border-blue-500 focus:outline-none',
                'rows': 5,
                'placeholder': 'Write your message here...'
            }),
        }