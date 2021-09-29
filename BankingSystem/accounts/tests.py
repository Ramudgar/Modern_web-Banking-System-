from django.test import TestCase




class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('your_server_ip:8000')
        self.assertEqual(response.status_code, 404)

    def test_login_loads_properly(self):
        """The login page loads properly"""
        response = self.client.get('your_server_ip:8000/accounts/login')
        self.assertEqual(response.status_code, 404)

    def test_register_loads_properly(self):
        """The register page loads properly"""
        response = self.client.get('your_server_ip:8000/accounts/register')
        self.assertEqual(response.status_code, 404)


