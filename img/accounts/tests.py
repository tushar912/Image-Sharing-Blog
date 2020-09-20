from django.test import TestCase
from django.contib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class LoginTestCase:
    
    def test_login_redirect_if_logged_in(self):
        response = self.client.get('chat:home')
        self.assertRedirects(response,'/accounts/login/?next=/')

        with self.settings(LOGIN_URL='/accounts/register/'):
            response = self.client.get('')
            self.assertRedirects(response, '/accounts/register/?next=/')



    def test_login_template:
        response = self.client.get(reverse('accounts:login'))
        self.assertTemplateUsed(response, 'registration/login.html')