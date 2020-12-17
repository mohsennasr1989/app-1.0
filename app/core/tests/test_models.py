from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """Test creating user with email is successful"""
        email = "test@domain.com"
        password = "testPass"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test user email is normalized"""
        email = 'test@domain.com'
        user = get_user_model().objects.create_user(email, 'testPass')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testPass')

    def test_create_new_superuser(self):
        """Test creating new superuser"""
        user = get_user_model().objects \
            .create_superuser('test@domain.com', 'testPass')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
