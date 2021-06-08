from django import forms
from ..models import Contact1


class ContactForm1(forms.ModelForm):
    class Meta:
        model = Contact1
        fields = ['firstname', 'lastname', 'email', 'subject', 'message']
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name'
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm1, self).__init__(*args, **kwargs)
        self.fields['firstname'].required = False
        self.fields['lastname'].required = False
