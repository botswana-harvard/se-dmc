from django.views.generic import TemplateView


class Contact(TemplateView):
    template_name = 'se_dmc/contact.html'