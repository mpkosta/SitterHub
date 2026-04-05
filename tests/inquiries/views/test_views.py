from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from sitters.models import Sitter
from inquiries.models import Inquiry

UserModel = get_user_model()

class InquiryViewsTests(TestCase):
    def setUp(self):
        self.client1 = UserModel.objects.create_user(
            username='client1',
            email='client1@abv.bg',
            password='testpassword123'
        )
        self.client2 = UserModel.objects.create_user(
            username='client2',
            email='client2@abv.bg',
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
            bio='Writing some description to pass validation.',
            experience=3,
            hourly_rate=15.00
        )
        self.inquiry = Inquiry.objects.create(
            user=self.client1,
            client_first_name='Ivan',
            client_last_name='Ivanov',
            client_phone='0888123456',
            sitter=self.sitter,
            message='I would like to hire you for next weekend.'
        )

    def test_inquiry_create_view_status_and_template(self):
        self.client.login(
            username='client1',
            password='testpassword123')
        response = self.client.get(reverse('inquiry-create', kwargs={'sitter_id': self.sitter.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inquiries/inquiry_form.html')

    def test_inquiry_create_view_post_success(self):
        self.client.login(
            username='client2',
            password='testpassword123')
        data = {
            'client_first_name': 'Gosho',
            'client_last_name': 'Georgiev',
            'client_phone': '0889289984',
            'message': 'I would like to hire you for tomorrow evening for 2 hours.'
        }
        response = self.client.post(reverse('inquiry-create', kwargs={'sitter_id': self.sitter.pk}), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Inquiry.objects.count(), 2)

    def test_inquiry_list_view_shows_client_inquiries(self):
        self.client.login(
            username='client1',
            password='testpassword123')
        response = self.client.get(reverse('inquiry-list'))
        self.assertIn(self.inquiry, response.context['inquiries'])

    def test_inquiry_list_view_shows_sitter_received_inquiries(self):
        self.client.login(
            username='sitter1',
            password='testpassword123')
        response = self.client.get(reverse('inquiry-list'))
        self.assertIn(self.inquiry, response.context['inquiries'])

    def test_inquiry_update_view_accessible_by_owner(self):
        self.client.login(
            username='client1',
            password='testpassword123')
        response = self.client.get(reverse('inquiry-edit', kwargs={'pk': self.inquiry.pk}))
        self.assertEqual(response.status_code, 200)

    def test_inquiry_update_view_not_accessible_by_other_user(self):
        self.client.login(
            username='client2',
            password='testpassword123')
        response = self.client.get(reverse('inquiry-edit', kwargs={'pk': self.inquiry.pk}))
        self.assertEqual(response.status_code, 404)

    def test_inquiry_delete_view_post_success(self):
        self.client.login(
            username='client1',
            password='testpassword123')
        response = self.client.post(reverse('inquiry-delete', kwargs={'pk': self.inquiry.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Inquiry.objects.count(), 0)

    def test_inquiry_delete_view_not_accessible_by_other_user(self):
        self.client.login(
            username='client2',
            password='testpassword123')
        response = self.client.post(reverse('inquiry-delete', kwargs={'pk': self.inquiry.pk}))
        self.assertEqual(response.status_code, 404)