from django.contrib import messages
from django.core.mail import send_mail
from django.db.models.functions import text
from django.http import HttpResponseRedirect, request
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from ..models import ContactForm
from ..models import contactinfo


class Contact(TemplateView):

    template_name = 'se_dmc/contact.html'
    form_class = contactinfo
    fields = ContactForm()
    initial = {'key': 'word'}

    def get(self, request, *args, **kwargs):
        form = contactinfo()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = contactinfo(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            self.fields.save()
            messages.success(request, "Thank you, message sent")
            print(first_name, last_name, email, subject, message)
            send_mail(subject, message, first_name, recipient_list=['wmathaka@bhp.org.bw'])

            return HttpResponseRedirect('contact')
        else:
            messages.error(request, "Message not sent, Some fields missing")
            args = {'form': form, 'text': text}
            return render(request, self.template_name, args)

