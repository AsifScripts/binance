from django.test import TestCase, Client

class URLTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_url(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_url(self):
        response = self.client.get('/')
        self.assertIn(response.status_code, [200, 302])  # 302 if not logged in

    def test_place_order_url(self):
        response = self.client.get('/place_order/')
        self.assertIn(response.status_code, [200, 302])

    def test_order_status_url(self):
        response = self.client.get('/order_status/')
        self.assertIn(response.status_code, [200, 302])

    def test_cancel_order_url(self):
        response = self.client.get('/cancel_order/')
        self.assertIn(response.status_code, [200, 302])