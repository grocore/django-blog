from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from datetime import date


class TestUserCreation(TestCase):
    '''
    Check if regular user and superuser creation process correct
    '''
    def test_create_user(self):
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_user(
            username='regular_user',
            email='regular@user.com',
            password='foobar123'
        )
        self.assertEqual(self.user.username, 'regular_user')
        self.assertEqual(self.user.email, 'regular@user.com')
        self.assertEqual(self.user.check_password('foobar123'), True)
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(username='', email='', password="foo")

    def test_create_superuser(self):
        self.user_model = get_user_model()
        self.admin_user = self.user_model.objects.create_superuser(username='superuser')
        self.assertEqual(self.admin_user.username, 'superuser')
        self.assertTrue(self.admin_user.is_active)
        self.assertTrue(self.admin_user.is_staff)
        self.assertTrue(self.admin_user.is_superuser)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username='failed_admin',
                email='super@user.com',
                password='foo',
                is_superuser=False
            )


class TestUserProfile(TestCase):
    '''
    Check if extended user model works correctly
    '''
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

    def test_user_content(self):
        self.user = User.objects.get(id=1)
        self.assertEqual(self.user.username, 'test_user')
        self.assertEqual(self.user.email, 'test@user.com')
        self.assertEqual(self.user.check_password('foobar123'), True)
        self.assertEqual(self.user.profile.bio, '0123456789' * 50)
        self.assertEqual(self.user.profile.birthday, date(1990, 10, 17))
        self.assertEqual(self.user.profile.location, 'Kyiv')
