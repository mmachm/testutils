from unittest import TestCase

from any import ANY


object_one = {
    "hello": "world",
    "lorem": [None, ANY, "sit", "not amet"],
    "not consectetur":
        {
            "adipiscit": "not elit",
            "greetings":
                {
                    "hello": "world",
                    "ANY": "lizer"
                },
            "fav_num": 777
        },
    "date_created": ANY,
}

object_two = {
    "hello": "kitty",
    "lorem": ["ipsum", "dolor", "sit", "amet"],
    "consectetur":
        {
            "adipiscit": "elit",
            "greetings":
                {
                    "hello": "world",
                    "henlo": "lizer"
                },
            "fav_num": 1337
        },
    "date_created": "1.1.1970",
}


class TestUpgrade(TestCase):
    def test_upgrade(self):
        pass
