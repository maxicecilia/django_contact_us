# coding: utf-8
from django.contrib.admin import ModelAdmin
from django.contrib.admin.util import unquote


class ContactUsAdmin(ModelAdmin):
    list_display = ('ts', 'from_name', 'from_email', )
    readonly_fields = ('ts', 'from_name', 'from_email', 'from_phone', 'message')
    fields = ('ts', 'from_name', 'from_email', 'from_phone', 'message')

    def change_view(self, request, object_id, extra_context=None):
        obj = self.get_object(request, unquote(object_id))
        if obj:
            obj.set_viewed(request.user)
        return super(ContactUsAdmin, self).change_view(request, object_id, extra_context=extra_context)
