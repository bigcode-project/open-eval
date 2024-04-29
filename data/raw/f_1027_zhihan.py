import requests
import json
import base64

def f_1027(data, url="http://your-api-url.com"):
    """
    Encode a Python dictionary into a JSON-formatted string and then the string into "ASCII."
    Send the encoded string to an API endpoint as a POST request.
    
    Parameters:
    data (dict): The Python dictionary to encode and send.
    url (str, optional): The API endpoint URL. Defaults to "http://your-api-url.com".
    
    Returns:
    Response: The response from the API endpoint.
    
    Requirements:
    - requests
    - json
    - base64
    
    Example:
    >>> data = {'name': 'John', 'age': 30, 'city': 'New York'}
    >>> response = f_1027(data, url="http://example-api-url.com")
    >>> print(response.status_code)
    """
    json_data = json.dumps(data)
    encoded_data = base64.b64encode(json_data.encode('ascii')).decode('ascii')
    response = requests.post(url, data={"payload": encoded_data})
    
    return response

import unittest
from unittest.mock import patch, Mock
import requests

# Mocking the requests.post method
def mock_post(*args, **kwargs):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = "OK"
    return mock_response

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    @patch('requests.post', side_effect=mock_post)
    def test_case_1(self, mock_post_method):
        data = {'name': 'John', 'age': 30, 'city': 'New York'}
        response = f_1027(data, url="http://mock-api-url.com")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")

    @patch('requests.post', side_effect=mock_post)
    def test_case_2(self, mock_post_method):
        data = {'task': 'Write code', 'status': 'completed'}
        response = f_1027(data, url="http://mock-api-url.com")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")

    @patch('requests.post', side_effect=mock_post)
    def test_case_3(self, mock_post_method):
        data = {}
        response = f_1027(data, url="http://mock-api-url.com")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")

    @patch('requests.post', side_effect=mock_post)
    def test_case_4(self, mock_post_method):
        data = {'fruit': 'apple', 'color': 'red', 'taste': 'sweet'}
        response = f_1027(data, url="http://mock-api-url.com")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")

    @patch('requests.post', side_effect=mock_post)
    def test_case_5(self, mock_post_method):
        data = {'country': 'USA', 'capital': 'Washington, D.C.'}
        response = f_1027(data, url="http://mock-api-url.com")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "OK")

if __name__ == "__main__":
    run_tests()