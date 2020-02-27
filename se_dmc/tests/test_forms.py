from django.test import SimpleTestCase
from se_dmc.models import Contact1


class TestForms(SimpleTestCase):

    def test_contact_form_valid_data(self):
        form = Contact1(
            firstname='test',
            lastname='test',
            email='test@gmail.com',
            subject='test',
            message='development'
        )

        self.assertTrue(form)




















