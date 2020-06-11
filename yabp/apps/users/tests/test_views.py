from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import date


class UserProfilePageTests(TestCase):

    def setUp(self):
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_user(
            username='test_user',
            email='test@user.com',
            password="foobar123"
        )
        self.user.profile.bio = '0123456789' * 50
        self.user.profile.birthday = date(1990, 10, 17)
        self.user.profile.location = 'Kyiv'
        self.user.save()
        self.client = Client()
        self.client.login(username='test_user', password='foobar123')

    def test_user_profile_page_status_code(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('user-profile'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('user-profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile.html')

    def test_user_profile_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(
            response, '<h5 class="card-header">Profile Information</h5>'
        )

    def test_user_profile_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/profile/')
        self.assertNotContains(
            response, '<title>Lorem ipsum dolor sit amet.</title>'
        )


class UserCreatePageTests(TestCase):

    def setUp(self):
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_user(
            username='test_user',
            email='test@user.com',
            password="foobar123"
        )
        self.user.profile.bio = '0123456789' * 50
        self.user.profile.birthday = date(1990, 10, 17)
        self.user.profile.location = 'Kyiv'
        self.user.save()
        self.client = Client()
        self.client.login(username='test_user', password='foobar123')

    def test_user_create_page_status_code(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('user-create'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('user-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_create.html')

    def test_user_create_page_contains_correct_html(self):
        response = self.client.get('/register/')
        self.assertContains(
            response, '<h5 class="card-header">Create a New Account</h5>'
        )

    def test_user_profile_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/register/')
        self.assertNotContains(
            response, '<title>Lorem ipsum dolor sit amet.</title>'
        )
