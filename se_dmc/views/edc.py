from django.views.generic import TemplateView


class ElectronicDataCapture(TemplateView):
    template_name = 'se_dmc/edc.html'