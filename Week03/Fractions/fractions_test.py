import unittest
from fractions import *

class TestSimplifyFractions(unittest.TestCase):
    def test_validate_fraction_object_is_a_tuple(self):
        with self.assertRaises(Exception) as exc:
            simplify_fraction([1, 2])
        # self.assertEqual('You should enter a tuple!', exc.exception)

    def test_when_nominator_equals_denominator_then_return_one(self):
        fraction = (3, 3)
        expected_result = (1, 1)
        self.assertEqual(simplify_fraction(fraction), expected_result)

    def test_when_denominator_is_zero_then_raise_exception(self):
        fraction = (1, 0)
        self.assertRaises(ZeroDivisionError, simplify_fraction, fraction)

    def test_when_nominator_and_denominator_both_prime_then_return_same_fraction(self):
        fraction = (2, 7)
        expected_result = (2, 7)
        self.assertEqual(simplify_fraction(fraction), expected_result)

    def test_when_larger_from_nominator_and_denominator_prime_then_return_same_fraction(self):
        fraction = (4, 7)
        expected_result = (4, 7)
        self.assertEqual(simplify_fraction(fraction), expected_result)

    def test_when_nominator_is_divisor_of_denominator_then_return_one_over_ratio(self):
        fraction = (2, 4)
        expected_result = (1, 2)
        self.assertEqual(simplify_fraction(fraction), expected_result)

    def test_when_denominator_is_divisor_of_nominator_then_return_ratio_over_one(self):
        fraction = (8, 4)
        expected_result = (2, 1)
        self.assertEqual(simplify_fraction(fraction), expected_result)

    def test_when_nominator_and_denominator_are_not_divisors_of_each_other_then_return_simplified(self):
        fraction = (63,462)
        expected_result = (3, 22)
        self.assertEqual(simplify_fraction(fraction), expected_result)

class TestCollectFractions(unittest.TestCase):
    def test_validate_input_object_is_a_list_of_two_tuples(self):
        with self.assertRaises(Exception) as exc:
            collect_fractions((1, 2))

    def test_when_one_of_denominators_is_zero_then_raise_error(self):
        fractions = [(1, 0), (8, 9)]
        self.assertRaises(ZeroDivisionError, collect_fractions, fractions)

    def test_when_denominators_are_equal_then_return_sum_of_nominators_over_denominator(self):
        fractions = [(1, 4), (2, 4)]
        expected_result = (3, 4)
        self.assertEqual(collect_fractions(fractions), expected_result)

    def test_when_denominators_are_not_equal(self):
        fractions = [(1, 7), (2, 6)]
        expected_result = (10, 21)
        self.assertEqual(collect_fractions(fractions), expected_result)

class TestSortFractions(unittest.TestCase):
    def test_validate_input_object_is_a_list_of_tuples(self):
        with self.assertRaises(Exception) as exc:
            sort_fractions((1, 2))

    def test_when_any_of_the_denominators_is_zero_then_raise_exception(self):
        with self.assertRaises(ZeroDivisionError):
            sort_fractions([(1, 1), (2, 0)])

    def test_when_list_then_return_sorted(self):
        fractions = [(2, 3), (1, 2), (1, 3)]
        expected_result = [(1, 3), (1, 2), (2, 3)]
        self.assertEqual(sort_fractions(fractions), expected_result)

if __name__ == '__main__':
    unittest.main()