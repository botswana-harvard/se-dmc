from django.views.generic import TemplateView


class Services(TemplateView):
    template_name = 'se_dmc/services.html'