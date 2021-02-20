from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password='123password',
            name='Some name'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='some@gmai.com',
            password='123password',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:authentication_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:authentication_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
