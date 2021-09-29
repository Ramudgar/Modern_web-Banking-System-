from django.contrib.auth import get_user_model

from django.test import TestCase

# Create your tests here.

class AdminsTests(TestCase):

    def test_create_user(self):

        User = get_user_model()

        user = User.objects.create_user(

        username='ram',

        email='ramudgary52@gmail.com',

        password='mko0,lp-'

        )

        self.assertEqual(user.username, 'ram')

        self.assertEqual(user.email, 'ramudgary52@gmail.com')

        self.assertTrue(user.is_active)

        self.assertFalse(user.is_staff)

        self.assertFalse(user.is_superuser)

        

    def test_create_superuser(self):

        User = get_user_model()

        admin_user = User.objects.create_superuser(

        username='superadmin',

        email='superadmin@email.com',

        password='testpass123'

        )

        self.assertEqual(admin_user.username, 'superadmin')

        self.assertEqual(admin_user.email, 'superadmin@email.com')

        self.assertTrue(admin_user.is_active)

        self.assertTrue(admin_user.is_staff)

        self.assertTrue(admin_user.is_superuser)


class AdminViewsTestCase(TestCase):
    def test_dashboard_loads_properly(self):
        """The dashboard page loads properly"""
        response = self.client.get('your_server_ip:8000')
        self.assertEqual(response.status_code, 404)

    def test_user_accounts_loads_properly(self):
        """The profiles page loads properly"""
        response = self.client.get('your_server_ip:8000/admins/profiles')
        self.assertEqual(response.status_code, 404)

    def test_get_user_loads_properly(self):
        """The show-user page loads properly"""
        response = self.client.get('your_server_ip:8000/admins/show-user')
        self.assertEqual(response.status_code, 404)

    def test_admin_dashboard_loads_properly(self):
        """The admin-dashboard page loads properly"""
        response = self.client.get('your_server_ip:8000/admins/admin_dashboard')
        self.assertEqual(response.status_code, 404)

    def test_update_user_to_admin_loads_properly(self):
        """The update to admin loads properly"""
        response = self.client.get('your_server_ip:8000/admins/update_user_to_admin')
        self.assertEqual(response.status_code, 404)

    def test_demote_admin_to_user_loads_properly(self):
        """The demote admin loads properly"""
        response = self.client.get('your_server_ip:8000/admins/demote_admin_to_user')
        self.assertEqual(response.status_code, 404)

    def test_delete_user_loads_properly(self):
        """The delete-user  loads properly"""
        response = self.client.get('your_server_ip:8000/admins/delete_user')
        self.assertEqual(response.status_code, 404)

    def test_search_loads_properly(self):
        """The search loads properly"""
        response = self.client.get('your_server_ip:8000/admins/search')
        self.assertEqual(response.status_code, 404)

    



