from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('account:login')
        self.signin_url = reverse('account:signin')
        self.user = User.objects.create_user(username='testuser', password='12345')
        
    def test_login_form_valid(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': '12345'
        })
            
        self.assertEqual(response.status_code, 302)
            
    def test_login_form_invalid(self):
        response = self.client.post(self.login_url, {
            'username':'wronguser',
            'password': 'wrongpassword'
        })
            
        self.assertEqual(response.status_code, 200)
    
    def test_signin_form_valid(self):
        response = self.client.post(self.signin_url, {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        })

        self.assertEqual(response.status_code, 302)

    def test_signin_form_invalid(self):
        response = self.client.post(self.signin_url, {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'abcdef123456',
            'password2': 'wrongpassword'
        })

        self.assertEqual(response.status_code, 200)
