# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status
from .models import Sujeto
from .serializers import SujetoSerializer

# tests for views

class BaseViewTest(APITestCase):

    @staticmethod
    def create_sujeto(cod='', nom='', formasocial=''):
        if cod != '' and nom != '':
            Sujeto.objects.create(cod=cod, nom=nom, formasocial=formasocial)

    def setUp(self):
        # create user
        self.username = 'test'
        self.email = 'test@test.com'
        self.password = 'Passw0rd'

        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.client = APIClient()

    def test_create_user(self):
        self.assertIsNotNone(User.objects.create_user('t3st', 'test@test.es', 'Passw0rd'))

    def test_create_supeuser(self):
        self.assertIsNotNone(User.objects.create_user('super', 'super@test.es', 'Passw0rd'))

    def test_login_user(self):
        self.assertTrue(self.client.login(username=self.username, password=self.password))

    def test_login_auth_token(self):
        self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
        self.assertTrue(self.client.force_authenticate(user=self.user))

class GetAllSujetos(BaseViewTest):

    def test_get_all_sujetos(self):
        """
        This test ensure that all sujetos added in the setUp method
        exist when we make a GET request to the sujetos / endpoint
        """
        # hit the API endpoint
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(
            reverse("sujetos-all")
        )
        # fetch the data from db
        expected = Sujeto.objects.all()
        serialized = SujetoSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)