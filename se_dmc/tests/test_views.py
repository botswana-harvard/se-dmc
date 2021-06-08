from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def test_home_view(self):
        client = Client()

        response = client.get(reverse('home_url'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'se_dmc/index.html')

    def test_about_view(self):
        client = Client()

        response = client.get(reverse('about'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'se_dmc/about.html')

    def test_services_view(self):
        client = Client()

        response = client.get(reverse('services'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'se_dmc/services.html')

    def test_work_view(self):
        client = Client()

        response = client.get(reverse('work'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'se_dmc/work.html')

    def test_contact_view(self):
        client = Client()

        response = client.get(reverse('contact'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'se_dmc/contact.html')
