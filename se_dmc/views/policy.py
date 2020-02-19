from django.views.generic import TemplateView


class Policy(TemplateView):
    template_name = 'se_dmc/policy.html'