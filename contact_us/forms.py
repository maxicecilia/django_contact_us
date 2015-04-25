# coding: utf-8
from django.forms import ModelForm
from models import SimpleContact


class ContactForm(ModelForm):
    '''
    Default form model for collect contact data.
    '''
    class Meta:
        model = SimpleContact
        fields = ('from_name', 'from_email', 'from_phone', 'message')


class SimpleContactForm(ModelForm):
    '''
    Simplified contact form, ignore phone input.
    '''
    class Meta:
        model = SimpleContact
        fields = ('from_name', 'from_email', 'message')
