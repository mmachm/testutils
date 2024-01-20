from collections import defaultdict
from unittest import TestCase

from any import ANY
from some import SOME

pairs_to_compare_equal = [
    (SOME(int), 1),
    (SOME(int), SOME(int),),
    (SOME(str), "123",),
    (SOME(str), SOME(str),),
    (SOME(dict), defaultdict(),),
    (SOME(dict), ANY,),

]

pairs_to_compare_unequal = [
    (SOME(str), SOME(int),),
    (SOME(str), 123,),
    (SOME(int), "123",),
    (SOME(dict), SOME(defaultdict),),
]

class TestSome(TestCase):
    def test_some(self):
        for pair in pairs_to_compare_equal:
            self.assertEqual(*pair)
            self.assertEqual(pair[1], pair[0])

        for pair in pairs_to_compare_unequal:
            self.assertNotEqual(*pair)
            self.assertNotEqual(pair[1], pair[0])

