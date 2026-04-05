from django.test import TestCase
from django.contrib.auth import get_user_model
from sitters.models import Sitter
from inquiries.models import Inquiry

UserModel = get_user_model()

class InquiryModelTests(TestCase):
    def setUp(self):
        self.client_user = UserModel.objects.create_user(
            username='client1',
            email='client1@abv.bg',
            password='testpassword123'
        )
        self.sitter_user = UserModel.objects.create_user(
            username='sitter1',
            email='sitter1@abv.bg',
            password='testpassword123'
        )
        self.sitter = Sitter.objects.create(
            user=self.sitter_user,
            sitter_first_name='Ivanka',
            sitter_last_name='Ivanova',
            bio='Adding some random text description to pass validation.',
            experience=2,
            hourly_rate=10.00
        )

    def test_inquiry_str_representation(self):
        inquiry = Inquiry.objects.create(
            user=self.client_user,
            client_first_name='Petar',
            client_last_name='Petrov',
            client_phone='0888123456',
            sitter=self.sitter,
            message='This message is written to pass validation.'
        )
        expected_str = "Petar Petrov is inquiring about Ivanka"
        self.assertEqual(str(inquiry), expected_str)

    def test_inquiry_creation_without_email(self):
        inquiry = Inquiry.objects.create(
            user=self.client_user,
            client_first_name='Georgi',
            client_last_name='Georgiev',
            client_phone='0884472971',
            sitter=self.sitter,
            message='I am writing some text message to pass validation.'
        )
        self.assertIsNone(inquiry.client_email)