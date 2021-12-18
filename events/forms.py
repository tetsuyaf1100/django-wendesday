from django import forms
from django.forms import ModelForm
from .models import Venue, Event

# Create a Event Form
class EventForm(ModelForm):
    class Meta:
        model = Event 
        fields = ('name', 'event_date', 'venue', 'manager', 'description', 'attendees')
        labels = {
            'name': '', 
            'event_date': '',
            'venue':'',
            'manager': '', 
            'description': '',
            'attendees': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event name'}),
            'event_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Even Date'}),
            'venue': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Venue name'}),
            'manager': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Manager'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
        }

# Create a Venue Form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')
        labels = {
            'name': '', 
            'address': '',
            'zip_code':'',
            'phone': '', 
            'web': '',
            'email_address': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Web Address'}),
            'email_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        }
