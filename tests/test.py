import requests
import unittest
from sqlalchemy import create_engine

class DockerComposeTestCase(unittest.TestCase):

    def test_post(self):
        expression = {'expression': "3+2"}
        result = requests.post('http://localhost:5000/add', data=expression)
        self.assertEqual(result.status_code, 200)

    def test_bad_post(self):
        incorrect = {"expression": "Hello xDD"}
        result = requests.post('http://localhost:5000/add', data=incorrect)
        self.assertNotEqual(result.status_code, 200)



if __name__ == '__main__':
    unittest.main()
