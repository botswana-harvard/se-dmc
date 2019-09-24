from django.views import generic


class IndexView(generic.ListView):
    template_name = 'se_dmc/index.html'
