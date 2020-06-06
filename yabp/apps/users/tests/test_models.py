from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from datetime import date


class TestUserCreation(TestCase):
    '''
    Check if regular user and superuser creation process correct
    '''
    def test_create_user(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(
            username='regular_user',
            email='regular@user.com',
            password='foobar'
        )
        self.assertEqual(user.username, 'regular_user')
        self.assertEqual(user.email, 'regular@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(username='', email='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(username='superuser')
        self.assertEqual(admin_user.username, 'superuser')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username='failed_admin',
                email='super@user.com',
                password='foo',
                is_superuser=False
            )


class ProfileTests(TestCase):
    '''
    Check if extended user model works correctly
    '''
    def setUp(self):
        user_model = get_user_model()
        user = user_model.objects.create(
            username='test_user',
            email='test@user.com',
            password="foobar"
        )
        user.profile.bio = '0123456789' * 50
        user.profile.birthday = date(1990, 10, 17)
        user.profile.location = 'Kyiv'
        user.save()

    def test_user_content(self):
        user = User.objects.get(id=1)
        self.assertEquals(user.username, 'test_user')
        self.assertEquals(user.email, 'test@user.com')
        self.assertEquals(user.password, 'foobar')
        self.assertEquals(user.profile.bio, '0123456789' * 50)
        self.assertEquals(user.profile.birthday, date(1990, 10, 17))
        self.assertEquals(user.profile.location, 'Kyiv')
