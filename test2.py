from flask import Flask
import unittest
from unittest.mock import patch
import requests
from faker import Faker
from app import getUser, addUser

class TestCases(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['JSON_AS_ASCII'] = False
        self.app.config['TESTING'] = True 
        print('Starting tests')

    def test_get_user(self):
        with self.app.app_context():
            resp = getUser(2)
        self.assertEqual(resp.json['name'], 'tolga')

    @patch('app.getRequestForm')
    def test_add_user(self, mockRequest):
        faker = Faker('tr_TR')
        name = faker.name()
        body = [{'name':name}]
        mockRequest.side_effect = body
        with self.app.app_context():
            response = addUser()
        self.assertEqual(response[1], 201)
        self.assertEqual(response[0].json['name'], name)

    def tearDown(self):
        print('Tests finished')

if __name__ == '__main__':
    unittest.main()
