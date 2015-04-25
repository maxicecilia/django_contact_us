
# Contact Us Project #
[![Build Status](https://travis-ci.org/maxicecilia/django_contact_us.svg)](https://travis-ci.org/maxicecilia/django_contact_us)
[![Coverage Status](https://coveralls.io/repos/maxicecilia/django_contact_us/badge.svg?branch=big_refactor)](https://coveralls.io/r/maxicecilia/django_contact_us?branch=big_refactor)


## About ##

Simple django app for displaying a contact form, reciving alerts emails and keep the messages in the admin site.

## Prerequisites ##

- Python 2.7
- pip
- virtualenv (virtualenvwrapper is recommended for use during development)
- Check requirements.txt!

## Installation / Usage ##


Install using pip like this:

pip install -e git+git@github.com:maxicecilia/django_contact_us.git@master#egg=django_contact_us

Add 'contact_us' to your INSTALLED_APPS setting

Add the view to your urls.py

    from contact_us.views import ContactUsFormView
    ...
    urlpatterns = patterns(
    ...
        url(r'^contact_us/', ContactUsFormView.as_view(), name='contact_us'),
    ...

You can set the template using **ContactUsFormView.as_view(template='my_template.html')** or redefine **contact_us/contact_form.html**

By default the form will redirect to /thanks/ unless you override the success_url or send a next attribute in the GET.

Optionally you can add the model to the admin, so you can see the messages:

    in your_project/admin.py
    from contact_us.admin import ContactUsAdmin
    from contact_us.models import SimpleContact
    
    admin.site.register(SimpleContact, ContactUsAdmin)





