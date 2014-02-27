from django.forms import ModelForm
from models import SimpleContact


class ContactForm(ModelForm):
    class Meta:
        model = SimpleContact
        fields = ('from_name', 'from_email', 'from_phone', 'message')


class SimpleContactForm(ModelForm):
    class Meta:
        model = SimpleContact
        fields = ('from_name', 'from_email', 'message')
