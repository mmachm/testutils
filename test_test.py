from unittest import TestCase
from unittest.mock import ANY

from merge import merge

expected_result = {
    "dict": {
        "Lorem ipsum": "Lorem ipsum dolor sit amet adipiscit elit I dont know latin",
        "Hello world": "Hello world",
        "test1": "test",
        "test2": "test",
        "test3": ANY,
    },
    "time": ANY
}
actual_result = {
    "dict": {
        "Lorem ipsum": "Lorem ipsum dolor sit amet adipiscit elit I dont know latin",
        "Hello world": "Bonjour le monde",
        "test1": "test",
        "test2": "test",
        "test3": "test",

    },
    "time": "today123"
}

class TestTest(TestCase):
    def test_test(self):
        self.assertEqual(expected_result, actual_result)

    def test_test_merged(self):
        self.assertEqual(*merge(expected_result, actual_result))