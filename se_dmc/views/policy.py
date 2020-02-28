from django.views.generic import TemplateView
from ..models import Policy


class Policies(TemplateView):
    template_name = 'se_dmc/policy.html'

    def get_context_data(self, **kwargs):
        context = super(Policies, self).get_context_data(**kwargs)
        context['policies'] = Policy.objects.all()
        return context








