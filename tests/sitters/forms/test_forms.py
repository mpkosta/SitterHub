from django.test import TestCase
from django.contrib.auth import get_user_model
from sitters.forms import SitterProfileUpdateForm, SitterCreateAdminForm
from services.models import ServiceGroup
from sitters.models import Sitter

UserModel = get_user_model()

class SitterFormTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='sitter1',
            email='sitter1@abv.bg',
            password='testpassword123'
        )
        self.service = ServiceGroup.objects.create(
            name='Babysitter',
            slug='babysitter'
        )

        self.sitter = Sitter.objects.create(
            user=self.user,
            sitter_first_name='Georgi',
            sitter_last_name='Georgiev',
            bio='This is some description of the sitter before updating.',
            experience=2,
            hourly_rate=10.00
        )

        self.valid_data = {
            'sitter_first_name': 'Ivan',
            'sitter_last_name': 'Ivanov',
            'bio': 'Making sure the description is long enough to pass the form validation process.',
            'services': [self.service.id],
            'experience': 5,
            'hourly_rate': 15.00,
        }

    def test_sitter_update_form_valid(self):
        form = SitterProfileUpdateForm(data=self.valid_data, instance=self.sitter)
        self.assertTrue(form.is_valid(), msg=form.errors)

    def test_sitter_update_form_invalid_name_contains_numbers(self):
        self.valid_data['sitter_first_name'] = 'Ivan123'
        form = SitterProfileUpdateForm(data=self.valid_data, instance=self.sitter)
        self.assertFalse(form.is_valid())
        self.assertIn('sitter_first_name', form.errors)

    def test_sitter_update_form_invalid_negative_experience(self):
        self.valid_data['experience'] = -2
        form = SitterProfileUpdateForm(data=self.valid_data, instance=self.sitter)
        self.assertFalse(form.is_valid())
        self.assertIn('experience', form.errors)

    def test_sitter_update_form_invalid_bio_too_short(self):
        self.valid_data['bio'] = 'Too short'
        form = SitterProfileUpdateForm(data=self.valid_data, instance=self.sitter)
        self.assertFalse(form.is_valid())
        self.assertIn('bio', form.errors)

    def test_sitter_update_form_hourly_rate_is_disabled(self):
        form = SitterProfileUpdateForm()
        self.assertTrue(form.fields['hourly_rate'].disabled)

    def test_admin_create_form_hourly_rate_is_not_disabled(self):
        form = SitterCreateAdminForm()
        self.assertFalse(form.fields['hourly_rate'].disabled)

    def test_admin_create_form_queryset_filters_correctly(self):
        UserModel.objects.create_user(
            username='sitter2',
            email='sitter2@abv.bg',
            password='testpassword123'
        )
        form = SitterCreateAdminForm()
        self.assertEqual(form.fields['user'].queryset.count(), 1)