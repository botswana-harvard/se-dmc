from django.test import  SimpleTestCase
from django.urls import resolve, reverse
from se_dmc.views import HomeView, About, Services, Work, contact

class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home_url')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, HomeView)

    def test_about_url_resolves(self):
        url = reverse('about')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, About)

    def test_services_url_resolves(self):
        url = reverse('services')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, Services)

    def test_work_url_resolves(self):
        url = reverse('work')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, Work)

    def test_contact_url_resolves(self):
        url = reverse('contact')
        print(resolve(url))
        self.assertEquals(resolve(url).func, contact)




