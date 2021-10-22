from django.test import TestCase
import json
import jwt
from rest_framework import status
from rest_framework.test import APIClient

class TestAPI(TestCase):

    def test_signUp(self):
        client = APIClient()
        response = client.post(
            '/user/', 
            {
                "username": "esteban",
                "password": "123456",
                "name": "esteban",
                "email": "esteban@misionTIC.com",
                "account": {
                    "lastChangeDate": "2021-09-23T10:25:43.511Z",
                    "balance": 20000,
                    "isActive": "true"
                }
            }, 
            format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual('refresh' in  response.data.keys(), True)
        self.assertEqual('access' in  response.data.keys(), True)

# Create your tests here.
