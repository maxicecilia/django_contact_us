# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
from django.contrib.sites.models import Site
from contact_us.forms import ContactForm, SimpleContactForm
from contact_us.models import SimpleContact


def _get_site():
    return Site.objects.create(domain='mock')


class ContactUsFormTestCase(unittest.TestCase):

    def setUp(self):
        self.form_data = {
            'from_name': 'arthur',
            'from_email': 'arthur@earth.com',
            'from_phone': '555-444',
            'message': "I think I'm a sofa",
        }

    def _test_required_field(self, field_name):
        """
        Check that the form does not validate without a given field.
        """
        del self.form_data[field_name]
        form = ContactForm(self.form_data)
        self.assertFalse(form.is_valid())
        self.assertIn(field_name, form.errors)

    def _test_optional_field(self, field_name):
        """
        Check that the form validate without a given field.
        """
        del self.form_data[field_name]
        form = ContactForm(self.form_data)
        self.assertTrue(form.is_valid())
        self.assertNotIn(field_name, form.errors)

    def test_notify_users(self):
        message = SimpleContact.objects.create(
            from_email='test@email.com', from_name='test',
            from_phone='555444', message='test message',
            site=_get_site())
        try:
            message.notify_users()
            self.assertTrue(True)
        except:
            self.assertTrue(False)


class ContactFormTestCase(ContactUsFormTestCase):
    """
    Unit tests for ``ContactForm`` class.
    """

    def test_from_name_field(self):
        self._test_optional_field('from_name')

    def test_from_email_field(self):
        self._test_optional_field('from_email')

    def test_from_phone_field(self):
        self._test_optional_field('from_phone')

    def test_message_field(self):
        self._test_required_field('message')

    def test_all_fields_valid(self):
        """
        When all required fields are supplied, the form is valid.
        """
        form = ContactForm(self.form_data)
        self.assertTrue(form.is_valid())

    def test_save(self):
        """
        A call to save() on a valid form sends the message.
        """
        form = ContactForm(self.form_data)
        self.assertTrue(form.is_valid())
        result = form.save(commit=False)
        result.site = _get_site()
        result.save()
        self.assertTrue(result)
        count = SimpleContact.objects.filter(
            from_name=self.form_data['from_name'],
            from_email=self.form_data['from_email'],
            from_phone=self.form_data['from_phone']).count()
        self.assertEqual(count, 1)


class SimpleContactFormTestCase(ContactUsFormTestCase):
    """
    Unit tests for ``ContactForm`` class.
    """

    def test_from_name_field(self):
        self._test_optional_field('from_name')

    def test_from_email_field(self):
        self._test_optional_field('from_email')

    def test_from_phone_field(self):
        self._test_optional_field('from_phone')

    def test_message_field(self):
        self._test_required_field('message')

    def test_all_fields_valid(self):
        """
        When all required fields are supplied, the form is valid.
        """
        form = SimpleContactForm(self.form_data)
        self.assertTrue(form.is_valid())

    def test_save(self):
        """
        A call to save() on a valid form sends the message.
        """
        form = SimpleContactForm(self.form_data)
        self.assertTrue(form.is_valid())
        result = form.save(commit=False)
        result.site = _get_site()
        result.save()
        self.assertTrue(result)
        count = SimpleContact.objects.filter(
            from_name=self.form_data['from_name'],
            from_email=self.form_data['from_email'],
            from_phone=None).count()
        self.assertEqual(count, 1)
