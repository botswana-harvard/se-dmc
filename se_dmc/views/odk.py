from django.views.generic import TemplateView


class OpenDataKit(TemplateView):
    template_name = 'se_dmc/odk.html'