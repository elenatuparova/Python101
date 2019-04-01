from polynomials import Monomials, Polynomials
import unittest

class TestMonomials(unittest.TestCase):

    def test_string_dunder(self):
        test_monomial = Monomials('3*x')
        expected_result = '3*x'
        self.assertEqual(str(test_monomial), expected_result)

    def test_add_dunder_when_power_is_zero(self):
        test_monomial1 = Monomials('3')
        test_monomial2 = Monomials('5')
        expected_result = Monomials('8')
        self.assertEqual(test_monomial1 + test_monomial2, expected_result)

    def test_add_dunder_when_power_is_one(self):
        test_monomial1 = Monomials('3*x')
        test_monomial2 = Monomials('5*x')
        expected_result = Monomials('8*x')
        self.assertEqual(test_monomial1 + test_monomial2, expected_result)

    def test_add_dunder_when_power_is_larger_than_one(self):
        test_monomial1 = Monomials('3*x^2')
        test_monomial2 = Monomials('5*x^2')
        expected_result = Monomials('8*x^2')
        self.assertEqual(test_monomial1 + test_monomial2, expected_result)

    def test_when_constant_then_return_zero(self):
        test_monomial = Monomials('3')
        expected_result = '0'
        self.assertEqual(test_monomial.calculate_derivative(), expected_result)

    def test_when_power_of_variable_is_one_then_return_coefficient(self):
        test_monomial = Monomials('3*x')
        expected_result = '3'
        self.assertEqual(test_monomial.calculate_derivative(), expected_result)

    def test_when_derivative_coefficient_is_larger_than_one_and_derivative_power_is_one(self):
        test_monomial = Monomials('x^2')
        expected_result = '2*x'
        self.assertEqual(test_monomial.calculate_derivative(), expected_result)

    def test_when_derivative_coefficient_is_larger_than_one_and_derivative_power_is_larger_than_one(self):
        test_monomial = Monomials('x^3')
        expected_result = '3*x^2'
        self.assertEqual(test_monomial.calculate_derivative(), expected_result)


class TestPolynomials(unittest.TestCase):

    def test_string_dunder(self):
        test_polynomial = Polynomials('3*x^2 + 2*x')
        expected_result = '3*x^2 + 2*x'
        self.assertEqual(str(test_polynomial), expected_result)

    def test_when_polynomial_consists_of_only_one_monomial_then_return_derivative_of_said_monomial(self):
        test_polynomial = Polynomials('2*x')
        expected_result = '2'
        self.assertEqual(test_polynomial.calculate_derivative(), expected_result)

    def test_when_polynomial_consists_of_more_than_one_monomials_and_has_a_constant(self):
        test_polynomial = Polynomials('2*x + 2')
        expected_result = '2'
        self.assertEqual(test_polynomial.calculate_derivative(), expected_result)

    def test_when_polynomial_consists_of_more_than_one_monomials_and_does_not_have_a_constant(self):
        test_polynomial = Polynomials('2*x^2 + 2*x')
        expected_result = '4*x + 2'
        self.assertEqual(test_polynomial.calculate_derivative(), expected_result)

    def test_when_polynomial_initially_has_more_than_one_monomial_of_the_same_power_then_sum_those_monomials(self):
        test_polynomial = Polynomials('2*x^3 + 5*x^3')
        expected_result = '21*x^2'
        self.assertEqual(test_polynomial.calculate_derivative(), expected_result)


if __name__ == '__main__':
    unittest.main()