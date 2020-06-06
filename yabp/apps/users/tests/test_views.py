from django.test import TestCase
from django.urls import reverse


class UserProfilePageTests(TestCase):

    def test_user_profile_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('user-profile'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('user-profile'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile.html')

    def test_user_profile_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(
            response, '<title>Yet Another Blogging Platform - Profile</title>'
        )

    def test_user_profile_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, '<title>Lorem ipsum dolor sit amet.</title>'
        )
