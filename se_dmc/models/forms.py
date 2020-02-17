from django import forms

from .contactform import ContactForm


class contactinfo(forms.ModelForm):

    class Meta:
        model = ContactForm
        fields = ['first_name', 'last_name', 'email', 'subject', 'message']


    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        subject = self.cleaned_data.get("subject")
        message = self.cleaned_data.get("message")

