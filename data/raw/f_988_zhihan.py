import json
import os
import hashlib
import base64
import time

def f_988(file_path, unknown_key):
    """
    Reads a JSON file, extracts a value specified by an 'unknown_key' within a nested structure, hashes this value using SHA256,
    and writes the base64-encoded hash to a new file with a timestamp in its name. The JSON should contain a specific 
    structure where the value to be hashed is under 'A' -> [unknown_key] -> 'maindata' -> [index 0] -> 'Info'.

    Parameters:
    - file_path (str): The file path to read the JSON data from.
    - unknown_key (str): The key to look for in the nested JSON structure under the top-level key 'A'. This key should 
                         lead to a list of dictionaries under 'maindata', with the first dictionary containing the 'Info' key.

    Returns:
    str: The absolute file path of the newly created file containing the hashed value.
    
    Requirements:
    - json
    - os
    - hashlib
    - base64
    - time
    
    Example:
    >>> json_file = '/path/to/file.json'
    >>> new_file = f_988(json_file, 'B')
    >>> print(f"Hashed data saved at: {new_file}")
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    value = list(data['A'][unknown_key].values())[0]['maindata'][0]['Info']
    hashed_value = hashlib.sha256(value.encode()).digest()
    hashed_str = base64.b64encode(hashed_value).decode()

    new_file_name = f"{unknown_key}_hashed_{int(time.time())}.txt"
    new_file_path = os.path.join(os.getcwd(), new_file_name)

    with open(new_file_path, 'w') as f:
        f.write(hashed_str)

    return new_file_path

import unittest
import os
import json
import hashlib
import base64
import time

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = f_988(path_1, 'B')
        self.assertTrue(os.path.exists(result))
        with open(result, 'r') as f:
            hashed_value = f.read()
        self.assertEqual(len(hashed_value), 44)

    def test_case_2(self):
        result = f_988(path_1, 'C')
        self.assertTrue(os.path.exists(result))
        with open(result, 'r') as f:
            hashed_value = f.read()
        self.assertEqual(len(hashed_value), 44)

    def test_case_3(self):
        result = f_988(path_2, 'D')
        self.assertTrue(os.path.exists(result))
        with open(result, 'r') as f:
            hashed_value = f.read()
        self.assertEqual(len(hashed_value), 44)

    def test_case_4(self):
        result = f_988(path_2, 'E')
        self.assertTrue(os.path.exists(result))
        with open(result, 'r') as f:
            hashed_value = f.read()
        self.assertEqual(len(hashed_value), 44)

    def test_case_5(self):
        with self.assertRaises(KeyError):
            f_988(path_1, 'Z')
if __name__ == "__main__":
    run_tests()