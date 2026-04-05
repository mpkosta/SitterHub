from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from sitters.models import Sitter, Language

UserModel = get_user_model()

class SitterModelTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='sitter1',
            email='sitter1@abv.bg',
            password='testpassword123'
        )

    def test_sitter_str_representation(self):
        sitter = Sitter.objects.create(
            user=self.user,
            sitter_first_name='Ivanka',
            sitter_last_name='Ivanova',
            bio='I really love children and I have 3 grandchildren!',
            experience=5,
            hourly_rate=15.50
        )
        expected_str = "Ivanka Ivanova"
        self.assertEqual(str(sitter), expected_str)

    def test_sitter_default_experience_is_zero(self):
        sitter = Sitter.objects.create(
            user=self.user,
            sitter_first_name='Petar',
            sitter_last_name='Petrov',
            bio='I am 18 years old and I raised my younger brother.',
            hourly_rate=10.00
        )
        self.assertEqual(sitter.experience, 0)

    def test_sitter_hourly_rate_max_digits(self):
        sitter = Sitter(
            user=self.user,
            sitter_first_name='Gosho',
            sitter_last_name='Peshov',
            bio='I am a third-year university student.',
            hourly_rate=1000.00
        )
        with self.assertRaises(ValidationError):
            sitter.full_clean()


class LanguageModelTests(TestCase):
    def test_language_str_representation(self):
        language = Language.objects.create(
            language_name='English')
        expected_str = 'English'
        self.assertEqual(str(language), expected_str)