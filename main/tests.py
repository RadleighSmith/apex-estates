from django.test import TestCase
from django.urls import reverse


class MessageViewsTestCase(TestCase):
    def test_about_view(self):
        url = reverse('about_us')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_contact_view(self):
        url = reverse('contact_us')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_send_message_view(self):
        url = reverse('send_message')
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'message': 'Test Message',
        }
        response = self.client.post(url, form_data)
        self.assertEqual(response.status_code, 302)