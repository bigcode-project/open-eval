import base64
from cryptography.fernet import Fernet

def f_1025(message, encryption_key):
    """
    Encrypt a message with a symmetric encryption key and then encode the encrypted message using base64.

    Parameters:
    message (str): The message to be encrypted and encoded.
    encryption_key (str): The key used for symmetric encryption. It should be a string of 32 bytes.

    Returns:
    str: The base64 encoded encrypted message.

    Requirements:
    - base64
    - cryptography.fernet

    Example:
    >>> encrypted_message = f_1025('Hello, World!', '01234567890123456789012345678901')
    >>> print(encrypted_message)
    """
    fernet = Fernet(base64.urlsafe_b64encode(encryption_key.encode()))
    encrypted_message = fernet.encrypt(message.encode())
    return base64.b64encode(encrypted_message).decode()

import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        # Test with a basic message and a valid encryption key.
        result = f_1025('Hello, World!', '01234567890123456789012345678901')
        self.assertIsInstance(result, str)
        self.assertNotEqual(result, 'Hello, World!')

    def test_case_2(self):
        # Test with an empty message and a valid encryption key.
        result = f_1025('', '01234567890123456789012345678901')
        self.assertIsInstance(result, str)
        self.assertNotEqual(result, '')

    def test_case_3(self):
        # Test with a numeric message and a valid encryption key.
        result = f_1025('1234567890', '01234567890123456789012345678901')
        self.assertIsInstance(result, str)
        self.assertNotEqual(result, '1234567890')

    def test_case_4(self):
        # Test with a long message and a valid encryption key.
        long_message = 'A' * 500
        result = f_1025(long_message, '01234567890123456789012345678901')
        self.assertIsInstance(result, str)
        self.assertNotEqual(result, long_message)

    def test_case_5(self):
        # Test with a basic message and a shorter encryption key (to test if the function handles key length issues).
        with self.assertRaises(Exception):
            f_1025('Hello, World!', '0123456789')

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()