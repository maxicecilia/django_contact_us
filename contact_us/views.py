# coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _

from forms import SimpleContactForm


def contact_us(request, extra_context=None, template=None):
    title = _(u"Contáctese con nosotros")
    if request.method == 'POST':
        form = SimpleContactForm(request.POST)
        if form.is_valid():
            form.save()
            form.instance.notify_users()
            form = None
            title = _(u"Muchas gracias")
    else:
        form = SimpleContactForm()

    context = {
        'title': title,
        'form': form,
    }
    context.update(extra_context or {})
    context_instance = RequestContext(request, current_app="contact_us")
    return render_to_response(template or 'contact_us/contact_form.html', context, context_instance=context_instance)
