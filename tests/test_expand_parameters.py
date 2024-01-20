from pprint import pprint
from unittest import TestCase

from expand_parameters import expand_parameters

dummy_test_1 = None


class TestExpandParameters(TestCase):

    def test_expand_parameters(self):
        default = 2

        class Dummy:
            @expand_parameters(
                [(i,) for i in range(5)] + [("hello", "world",), ("hello", "world", "!")],
                default_input_index=default
            )
            def dummy_test(self, x="test", y="test"):
                return x, y

            dummy_test_1 # <- this would fail if Dummy was just a function, why??


        dummy = Dummy()

        self.assertEqual((default, "test"), dummy.dummy_test())

        self.assertEqual((0, "test"), dummy.dummy_test_0())
        self.assertEqual((1, "test"), dummy.dummy_test_1())
        self.assertEqual((2, "test"), dummy.dummy_test_2())
        self.assertEqual((3, "test"), dummy.dummy_test_3())
        self.assertEqual((4, "test"), dummy.dummy_test_4())

        self.assertEqual(("hello", "world"), dummy.dummy_test_5_hello())

        with self.assertRaises(TypeError):
            self.assertEqual(("hello", "world"), dummy.dummy_test_6_hello())


    def test_the_main_values_do_not_leak_to_defaults_for_others(self):
        class Dummy:
            @expand_parameters(
                [
                    ("hello", "world"),
                    ("hello",)
                ],
                default_input_index=0
            )
            def dummy_test(self, x="test", y="test"):
                return x, y
            pprint(locals())

        dummy=Dummy()

        self.assertEqual(("hello", "world"), dummy.dummy_test_0_hello())
        self.assertEqual(("hello", "test"), dummy.dummy_test_1_hello())

        print("""
By the way accessing the newly injected local variables like print(dummy_test_1)
while still inside the definition of the class does give the function, as it should.
But trying to do this if the surrounding class was actually just a function 
gives a NameError despite the fact that 'dummy_test_1' is in locals().
Python probably optimizes itself upon compilation to immediately look in the 
enclosing/global scope as the variable dummy_test_1 is (only) apparently 
a free/global variable. It is pretty cursed. According to documentation:

Free variables are returned by locals() when it is called in function blocks, 
but not in class blocks. 

This sounds to me like the opposite of what I get, actually.
        """)