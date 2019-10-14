from django.views.generic import TemplateView


class About(TemplateView):
    template_name = 'se_dmc/about.html'