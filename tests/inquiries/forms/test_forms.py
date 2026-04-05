from django.test import TestCase
from inquiries.forms import InquiryForm

class InquiryFormTests(TestCase):
    def setUp(self):
        self.valid_data = {
            'client_first_name': 'Ivan',
            'client_last_name': 'Ivanov',
            'client_phone': '0888298471',
            'client_email': 'client1@abv.bg',
            'message': 'I would like to hire you for 3 hours for the upcoming weekend.'
        }

    def test_inquiry_form_valid(self):
        form = InquiryForm(data=self.valid_data)
        self.assertTrue(form.is_valid(), msg=form.errors)

    def test_inquiry_form_invalid_phone_length(self):
        self.valid_data['client_phone'] = '00331'
        form = InquiryForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('client_phone', form.errors)

    def test_inquiry_form_invalid_message_length(self):
        self.valid_data['message'] = 'Short message'
        form = InquiryForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors)

    def test_inquiry_form_valid_without_email(self):
        self.valid_data.pop('client_email')
        form = InquiryForm(data=self.valid_data)
        self.assertTrue(form.is_valid(), msg=form.errors)