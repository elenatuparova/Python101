import unittest
from decorators import *

class TestAcceptsDecorator(unittest.TestCase):

    def test_say_hello_when_name_is_not_str_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            say_hello(1)

    def test_deposit_when_first_argument_is_not_str_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            deposit(1, 100)

    def test_deposit_when_second_argument_is_not_str_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            deposit('Roza', '100')


class TestEncryptDecorator(unittest.TestCase):

    def test_get_low_encryption_with_step_two(self):
        expected_result = 'Igv igv igv nqy'
        self.assertEqual(get_low(), expected_result)


if __name__ == '__main__':
    unittest.main()