from django.views.generic import TemplateView


class RedCap(TemplateView):
    template_name = 'se_dmc/redcap.html'