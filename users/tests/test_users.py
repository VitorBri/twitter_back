from django.test import TestCase
from users.factories import UsersFactory


class TestUserModel(TestCase):
    def setUp(self):
        self.user = UsersFactory(username="joao", password="123")

    def test_user_created(self):
        self.assertEqual(self.user.username, "joao")
        self.assertTrue(self.user.check_password("123"))
        self.assertIsNotNone(self.user.pk) 