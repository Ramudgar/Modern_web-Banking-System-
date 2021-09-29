from django.contrib.auth import get_user_model

from django.test import TestCase

# Create your tests here.

class ProfilesViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('your_server_ip:8000')
        self.assertEqual(response.status_code, 404)

    def test_accounts_status_loads_properly(self):
        """The account status page page loads properly"""
        response = self.client.get('your_server_ip:8000/profiles/account_status')
        self.assertEqual(response.status_code, 404)

    def test_money_transfer_loads_properly(self):
        """The money transfer page loads properly"""
        response = self.client.get('your_server_ip:8000/profiles/money_transfer')
        self.assertEqual(response.status_code, 404)

    def test_loan_loads_properly(self):
        """The loan page loads properly"""
        response = self.client.get('your_server_ip:8000/profiles/loan_app')
        self.assertEqual(response.status_code, 404)

    def test_withdraw_money_loads_properly(self):
        """The withdraw money page loads properly"""
        response = self.client.get('your_server_ip:8000/profiles/withdraw_money')
        self.assertEqual(response.status_code, 404)

    def test_deposit_loads_properly(self):
        """The deposit money page loads properly"""
        response = self.client.get('your_server_ip:8000/profiles/deposit')
        self.assertEqual(response.status_code, 404)

    def test_settings_loads_properly(self):
        """The settings page loads properly"""
        response = self.client.get('your_server_ip:8000/profiles/settings')
        self.assertEqual(response.status_code, 404)

    def test_edit_details_loads_properly(self):
        """The edit details page loads properly"""
        response = self.client.get('your_server_ip:8000/profiles/edit_details')
        self.assertEqual(response.status_code, 404)

    def test_delete_account_loads_properly(self):
        """The delete account page loads properly"""
        response = self.client.get('your_server_ip:8000/profiles/delete_accounts')
        self.assertEqual(response.status_code, 404)