from django.views.generic import TemplateView


class Cancer(TemplateView):
    template_name = 'se_dmc/cancer.html'
