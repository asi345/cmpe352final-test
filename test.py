import unittest
import requests

class TestCases(unittest.TestCase):

    def setUp(self):
        print('Starting tests')

    def test_get_user(self):
        response = requests.get('http://127.0.0.1:5000/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'tolga')

    def test_add_user(self):
        item = {'name':'mehdi'}
        response = requests.post('http://127.0.0.1:5000/add', data=item)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['name'], 'mehdi')

    def tearDown(self):
        print('Tests finished')
