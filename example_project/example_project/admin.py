# coding: utf-8
from django.contrib import admin
from contact_us.admin import ContactUsAdmin
from contact_us.models import SimpleContact

admin.site.register(SimpleContact, ContactUsAdmin)
