from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.

class PostTests(TestCase):

    def helper_status_200(self, url_name, path=None):
        url = reverse(url_name, args=path)
        response = self.client.get(url)
        actual = response.status_code
        expected = 200
        self.assertEqual(actual, expected)

    def test_HomePage_status(self):
        self.helper_status_200('home')

    # def test_DetailsPage_status(self):
    #     self.helper_status_200('details', [4])


    def helper_template_used(self, url_name, path=None):
        url = reverse(url_name, args=path)
        response = self.client.get(url)
        self.assertTemplateUsed(response, url_name+'.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_home_page_template(self):
        self.helper_template_used('home')

    # def test_details_page_template(self):
    #     self.helper_template_used('details', [4])
