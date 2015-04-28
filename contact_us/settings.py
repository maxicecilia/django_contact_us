from django.conf import settings

# Valid options: full | simple
FORM_STYLE = getattr(settings, 'CONTACT_US_FORM_STYLE', 'full')

# Default action value used to log
LOG_ACTION_VIEW = getattr(settings, 'CONTACT_US_LOG_ACTION_VIEW', 4)

# Force mails to this list if not empty.
RECIPIENTS_LIST = getattr(settings, 'CONTACT_US_RECIPIENTS_LIST', [])

# Set the fail_silently flag for send_email
EMAIL_FAIL_SILENTLY = getattr(settings, 'CONTACT_US_EMAIL_FAIL_SILENTLY', False)
