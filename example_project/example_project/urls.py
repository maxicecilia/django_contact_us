# coding: utf-8
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from contact_us.views import ContactUsFormView
from contact_us.forms import SimpleContactForm

urlpatterns = [
    url(r'^contact_us/', ContactUsFormView.as_view(), name='contact_us'),
    url(r'^contact_us_simplified/', ContactUsFormView.as_view(
        form_class=SimpleContactForm), name='contact_us_simplified'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^thanks/$', TemplateView.as_view(template_name="thanks.html")),
    url(r'^(/)*$', TemplateView.as_view(template_name="index.html")),
]
