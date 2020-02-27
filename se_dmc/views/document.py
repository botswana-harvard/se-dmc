from django.views.generic import TemplateView
from django.shortcuts import render
from ..models import Document

# class Document(TemplateView):
  #  template_name = 'se_dmc/document.html'

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'se_dmc/document.html', {
        'documents': documents
    })

class Documents(TemplateView):
    template_name = 'se_dmc/document.html'

    def get_context_data(self, **kwargs):
        context = super(Documents, self).get_context_data(**kwargs)
        context['documents'] = Document.objects.all()
        return context


