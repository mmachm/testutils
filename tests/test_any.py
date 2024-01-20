from unittest import TestCase
from any import ANY, AnyOneThing, Any

values_to_test = [None, True, False, type, ANY, 123, "123", [123], {"123": 123}]

class TestAny(TestCase):
    def test_any_equal(self):
        for value in values_to_test:
            self.assertTrue(value == ANY)
            self.assertTrue(ANY == value)

    def test_any_not_equal(self):
        for value in values_to_test:
            self.assertFalse(value != ANY)
            self.assertFalse(ANY != value)

    def test_any_one_thing_recursion(self):
        a = AnyOneThing()
        # this is deliberately twice
        self.assertEqual(a, a)
        self.assertEqual(a, a)

    def test_any_one_thing_against_any(self):
        a = AnyOneThing()
        self.assertEqual(a, Any())
        self.assertEqual(a, Any())

    def test_any_one_thing(self):
        object = AnyOneThing()
        expected_response = {
            "mushroom stroganoff": object,
            "chicken kyiv": object,
        }
        response_one = {
            "mushroom stroganoff": 1,
            "chicken kyiv": 1,
        }
        response_two = {
            "mushroom stroganoff": 1,
            "chicken kyiv": 2,
        }

        self.assertEqual(expected_response, response_one)
        self.assertNotEqual(expected_response, response_two)

