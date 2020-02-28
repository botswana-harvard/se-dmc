from django.views.generic import TemplateView
from django.conf import settings

from django.core.checks import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..forms import ContactForm1

class Contact(TemplateView):
    template_name = 'se_dmc/contact.html'

    def index(request):

        if request.method == 'POST':
            message = request.POST['message']
            send_mail('Contact Form',
                      message,
                      settings.EMAIL_HOST_USER,
                      ['thatokgamaetsile@gmail.com'],
                      fail_silently=False)
        return render(request, 'se_dmc/contact.html')

def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm1(request.POST)

        if contact_form.is_valid():

            firstname = contact_form.cleaned_data['firstname']
            lastname = contact_form.cleaned_data['lastname']
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']

            recipients = ['tkgamaetsile@bhp.org.bw']
            if email:
                recipients.append(email)

            content = 'Message: '+message+' \nFirst-Name: '+firstname+'\nLast-Name: '+lastname

            send_mail(subject, content, email, recipients)
            contact_form.save()
            print('Message sent successfully.')
            return redirect('contact')
        else:
            print('Error sending your Message')

    else:
        contact_form = ContactForm1(request.POST)

    context = {
        "contact_form": contact_form,
    }
    template = 'se_dmc/contact.html'
    return render(request, template, context)




