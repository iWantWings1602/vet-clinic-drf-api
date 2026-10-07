from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Owner, Pet

class PetPermissionsTests(APITestCase):
    def setUp(self):
        self.owner_user = User.objects.create_user(username='owner', password='pass12345')
        self.other_user = User.objects.create_user(username='other', password='pass12345')

        self.owner_profile = Owner.objects.create(user=self.owner_user, name='Test Owner', phone='+111')

        self.pet = Pet.objects.create(owner=self.owner_profile, name='Bobik', species='dog', birth_year=2021)

        self.url = f'/api/pets/{self.pet.pk}/'

    def test_anyone_can_read(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_cannot_edit(self):
        response = self.client.patch(self.url, {'name': 'New Name'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_other_user_cannot_edit(self):
        self.client.force_authenticate(user=self.other_user)
        response = self.client.patch(self.url, {'name': 'New Name'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_owner_can_edit(self):
        self.client.force_authenticate(user=self.owner_user)
        response = self.client.patch(self.url, {'name': 'Valid Name'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)