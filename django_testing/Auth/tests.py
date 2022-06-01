
from django.test import TestCase, Client
from .models import UserAccount
from .Serializeres.user_serializer import UserSerializer, UserRegisterSerializer
from rest_framework.test import APIClient
from mixer.backend.django import mixer
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

# initialize api client app
client = Client()


# Model test


class UserTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        User = get_user_model()
        self.my_user = User.objects.create_user(
            name="nas1", email="nas1@gmail.com", password="password")
        self.token = Token.objects.create(user=self.my_user)
        self.client.credentials(HTTP_AUTHORIZATION="Token "+self.token.key)

    def test_users(self):
        response = self.client.get("/users/",)
        assert response.status_code == 200


class GetAllUsers(TestCase):
    def setUp(self):
        self.client = APIClient()
        User = get_user_model()
        self.my_user = User.objects.create_user(
            name="nas1", email="nas1@gmail.com", password="password")
        self.token = Token.objects.create(user=self.my_user)
        self.client.credentials(HTTP_AUTHORIZATION="Token "+self.token.key)

    def test_get_all_users(self):
        # Make an authenticated request to the view...
        response = self.client.get('/users/')
        users = UserAccount.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)

class RegistrationTest(TestCase):
    pass