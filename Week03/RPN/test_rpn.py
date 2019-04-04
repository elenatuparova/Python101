import unittest
from rpn import rpn_calculate
from rpn import get_float_list
from rpn import pop_last_two

class TestReversePolishNotation(unittest.TestCase):
    def test_when_single_digit_is_passed_then_return_the_same_digit(self):
        expr = '45'
        expected_result = 45
        self.assertEqual(rpn_calculate(expr), expected_result)

    def test_when_two_numbers_are_passed_then_return_sum_of_them(self):
        expr = '4 8 +'
        expected_result = 12
        self.assertEqual(rpn_calculate(expr), expected_result)

    def test_when_substraction_of_two_numbers_then_return_the_difference(self):
        expr = '7 3 -'
        expected_result = 4
        self.assertEqual(rpn_calculate(expr), expected_result)

    def test_when_multiplication_of_two_numbers_then_return_the_product(self):
        expr = '7 3 *'
        expected_result = 21
        self.assertEqual(rpn_calculate(expr), expected_result)

    def test_when_division_of_two_numbers_then_return_the_ratio(self):
        expr = '6 3 /'
        expected_result = 2
        self.assertEqual(rpn_calculate(expr), expected_result)

    def test_when_sqrt_of_number_then_return_the_square_root(self):
        expr = '9 SQRT'
        expected_result = 3
        self.assertEqual(rpn_calculate(expr), expected_result)

    def test_when_minus_after_single_number_then_return_negative_of_number(self):
        expr = '4 -'
        expected_result = -4
        self.assertEqual(rpn_calculate(expr), expected_result)

    def test_when_max_then_return_maximum_of_all_previous_numbers(self):
        expr = '4 5 9 1 0 MAX'
        expected_result = 9
        self.assertEqual(rpn_calculate(expr), expected_result)

    def test_when_min_then_return_maximum_of_all_previous_numbers(self):
        expr = '4 5 9 1 0 MIN'
        expected_result = 0
        self.assertEqual(rpn_calculate(expr), expected_result)

    def test_when_some_list_then_return_list_of_floats(self):
        lst = ['4.5', '9', '1']
        expected_result = [4.5, 9.0, 1.0]
        self.assertEqual(get_float_list(lst), expected_result)

    def test_when_pop_twice_then_remove_last_two_elements_from_list(self):
        lst = [1, 2, 3]
        expected_result = [1]
        self.assertEqual(pop_last_two(lst), expected_result)


if __name__ == '__main__':
    unittest.main()