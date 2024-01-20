from unittest.mock import ANY
import pytest

def test_pytest():
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