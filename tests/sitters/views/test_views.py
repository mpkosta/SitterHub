from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from sitters.models import Sitter
from services.models import ServiceGroup

UserModel = get_user_model()


class SitterViewsTests(TestCase):
    def setUp(self):
        self.regular_user = UserModel.objects.create_user(
            username='client1',
            email='client1@abv.bg',
            password='testpassword123'
        )

        self.staff_user = UserModel.objects.create_user(
            username='admin1',
            email='admin1@abv.bg',
            password='testpassword123',
            is_staff=True
        )

        self.service = ServiceGroup.objects.create(
            name='Babysitter',
            slug='babysitter'
        )

        self.sitter = Sitter.objects.create(
            user=self.regular_user,
            sitter_first_name='Ivanka',
            sitter_last_name='Ivanova',
            bio='Experienced babysitter working 20 years with children.',
            experience=3,
            hourly_rate=12.00
        )
        self.sitter.services.add(self.service)

    def test_sitter_list_view_pagination(self):
        for i in range(15):
            user = UserModel.objects.create_user(
                username=f'sitter{i}',
                email=f'sitter{i}@abv.bg',
                password='testpassword123'
            )
            Sitter.objects.create(
                user=user,
                sitter_first_name=f'Name{i}',
                sitter_last_name='Last',
                bio='Bio',
                hourly_rate=10
            )

        response = self.client.get(reverse('sitters-list'))
        self.assertTrue(response.context['is_paginated'])
        self.assertEqual(len(response.context['sitters']), 10)

    def test_sitter_list_view_filters_by_service_category(self):
        response = self.client.get(reverse('sitters-list'), {'service_category_slug': 'babysitter'})
        self.assertIn(self.sitter, response.context['sitters'])

    def test_sitter_update_view_accessible_only_by_owner(self):
        UserModel.objects.create_user(
            username='client2',
            email='client2@abv.bg',
            password='testpassword123'
        )
        self.client.login(
            username='client2',
            password='testpassword123')

        response = self.client.get(reverse('sitter-edit', kwargs={'pk': self.sitter.pk}))
        self.assertEqual(response.status_code, 403)

    def test_sitter_delete_view_accessible_by_staff(self):
        self.client.login(
            username='admin1',
            password='testpassword123')
        response = self.client.get(reverse('sitter-delete', kwargs={'pk': self.sitter.pk}))
        self.assertEqual(response.status_code, 200)