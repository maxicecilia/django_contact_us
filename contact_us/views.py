# coding: utf-8
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render_to_response
from django.views.generic.edit import FormView
from forms import ContactForm


class ContactUsFormView(FormView):
    form_class = ContactForm
    success_url = '/thanks/'
    template_name = 'contact_us/contact_form.html'

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.site = get_current_site(self.request)
        obj.save()
        form.instance.notify_users()
        return super(ContactUsFormView, self).form_valid(form)

    def get_success_url(self):
        next_url = self.request.GET.get('next', None)
        if next_url:
            return "{}".format(next_url)
        return super(ContactUsFormView, self).get_success_url()