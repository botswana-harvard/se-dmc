from django.views.generic import TemplateView
from ..models import Address

class Contact(TemplateView):
    template_name = 'se_dmc/contact.html'
    model = Address
    context_object_name = 'contact_details'