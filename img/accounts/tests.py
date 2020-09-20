from django.test import TestCase
from django.contib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class LoginTestCase(TestCase):
    
    def test_login_redirect_if_logged_in(self):
        response = self.client.get('chat:home')
        self.assertRedirects(response,'/accounts/login/?next=/')

        with self.settings(LOGIN_URL='/accounts/register/'):
            response = self.client.get('')
            self.assertRedirects(response, '/accounts/register/?next=/')



    def test_login_template:
        response = self.client.get(reverse('accounts:login'))
        self.assertTemplateUsed(response, 'registration/login.html')


class RegisterationTestCase(TestCase):

    def test_redirect_if_user_logged_in(self):
        _user = User.objects.create(username='abc', email='abc@test.com')
        _user.set_password('abc')
        _user.save()
        self.client.login(username='abc', password='abc')
        response = self.client.get(reverse('accounts:register'))
        self.assertRedirects(response, reverse('chat:home'))

    def test_valid_registration(self):
        valid_reg_data = {
            'username': 'john',
            'email': 'john@test.com',
            'first_name': 'john',
            'last_name': 'doe',
            'password1': '@secret123',
            'password2': '@secret123'
        }
        response = self.client.post(reverse('accounts:register'), valid_reg_data)
        self.assertRedirects(response, reverse('chat:home'))
        self.assertEqual(User.objects.count(), 1)        

    
    def test_invalid_registration(self):
        invalid_reg_data = [
            {
                
                'username': 'john',
                'email': 'john@test.com',
                'first_name': 'john',
                'last_name': 'doe',
                'password1': 'secret12',
                'password2': 'secret123'
            },
            {
                
                'username': 'john',
                'email': 'johntest.com',
                'first_name': 'john',
                'last_name': 'doe',
                'password1': 'secret123',
                'password2': 'secret123'
            },
            {
                
                'username': '!john',
                'email': 'john@test.com',
                'first_name': 'john',
                'last_name': 'doe',
                'password1': 'secret12',
                'password2': 'secret123'
            },

        ]
        for invalid_form in invalid_reg_data:
            response = self.client.post(reverse('accounts:register'), invalid_form)
            self.assertEqual(response.status_code, 200)

    def test_register_page_templates(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertTemplateUsed(response, 'registration/register.html') 