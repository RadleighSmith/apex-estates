from django.test import TestCase
from django.urls import reverse


class MessageViewsTestCase(TestCase):
    """
    Test case for message-related views.
    """

    def test_about_view(self):
        """
        Test the about view.

        This test checks if the about view returns a status code of 200 (OK).
        """
        url = reverse('about_us')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_contact_view(self):
        """
        Test the contact view.

        This test checks if the contact view returns a status code of 200 (OK).
        """
        url = reverse('contact_us')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_send_message_view(self):
        """
        Test the send message view.

        This test checks if the send message view returns a redirect status
        code (302) after successfully sending a message.
        """
        url = reverse('send_message')
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'message': 'Test Message',
        }
        response = self.client.post(url, form_data)
        self.assertEqual(response.status_code, 302)
