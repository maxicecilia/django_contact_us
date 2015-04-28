# coding: utf-8
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from django.db import models
from django.template import loader, Context
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext as _

from settings import LOG_ACTION_VIEW, RECIPIENTS_LIST, EMAIL_FAIL_SILENTLY


class SimpleContact(models.Model):
    from_email = models.EmailField(_(u'Email'), blank=True, null=True)
    from_name = models.CharField(_(u'Nombre'), max_length=64, blank=True, null=True)
    from_phone = models.CharField(_(u'Teléfono'), max_length=64, blank=True, null=True)
    message = models.TextField(_(u'Mensaje'))
    site = models.ForeignKey(Site)
    ts = models.DateTimeField(_(u'Timestamp'), auto_now=True, editable=False)

    class Meta:
        ordering = ('-ts', )
        verbose_name = _(u'Contácto')
        verbose_name_plural = _(u'Contáctos')

    def set_viewed(self, user):
        LogEntry.objects.log_action(
            user_id=user.pk,
            content_type_id=ContentType.objects.get_for_model(self).pk,
            object_id=self.pk,
            object_repr=force_unicode(self),
            action_flag=LOG_ACTION_VIEW,
            change_message=_(u"Leído por {0}".format(force_unicode(user))))

    def get_viewed(self, user):
        return (LogEntry.objects.filter(
            object_id=self.pk,
            content_type__id__exact=ContentType.objects.get_for_model(self).pk,
            action_flag=LOG_ACTION_VIEW, )
            .exists())

    def notify_users(self, email_template=None, subject_template=None, recipients=None):
        """
        Sends an email to all users who have permission to view the model in admin.
        First line of the template is the subject
        """
        # Render emails
        email_template = loader.get_template(
            email_template or "contact_us/notification_email.txt")
        subject_template = loader.get_template(
            subject_template or "contact_us/notification_email_subject.txt")
        context = Context({'obj': self})
        body = email_template.render(context)
        subject = subject_template.render(context)
        # Get list of receivers
        if recipients:
            recipient_list = recipients
        elif len(RECIPIENTS_LIST) > 0:
            recipient_list = RECIPIENTS_LIST
        else:
            recipient_list = []
            for u in User.objects.filter(is_staff=True, is_active=True).exclude(email=""):
                if u.has_perm("contact_us.change_simplecontact"):
                    recipient_list.append(u.email)
        # Send email
        send_mail(
            subject, body, settings.DEFAULT_FROM_EMAIL,
            recipient_list, fail_silently=EMAIL_FAIL_SILENTLY, )

    def __unicode__(self):
        return '{0} ({1})'.format(self.ts, self.from_email)

    @models.permalink
    def get_absolute_url(self):
        return ('admin:contact_us_simplecontact_change', [str(self.id)])
