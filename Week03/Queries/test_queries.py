import unittest
from queries import *

class TestFilter(unittest.TestCase):

    def test_when_filter_not_valid_then_raise_exception(self):
        with self.assertRaises(Exception) as exc:
            filter('example_data.csv', name='Diana')
            
    def test_when_one_default_filter_is_passed(self):
        expected_result = [['Diana Harris', 'lime', 'Martin-Barnes', 'timothy81@gmail.com', '1-860-251-9980x6941', '5354']]
        self.assertEqual(filter('example_data.csv', full_name='Diana Harris'), expected_result)

    def test_when_more_than_one_default_filters_are_passed(self):
        expected_result = [['Diana Harris', 'lime', 'Martin-Barnes', 'timothy81@gmail.com', '1-860-251-9980x6941', '5354']]
        self.assertEqual(filter('example_data.csv',favourite_color="lime", company_name='Martin-Barnes'), expected_result)

    def test_when_startswith_filter_is_passed(self):
        expected_result = [['Diana Harris', 'lime', 'Martin-Barnes', 'timothy81@gmail.com', '1-860-251-9980x6941', '5354']]
        self.assertEqual(filter('example_data.csv', full_name__startswith="Diana"), expected_result)

    def test_when_contains_filter_is_passed(self):
        expected_result = [['Kevin Flores', 'fuchsia', 'Martinez Ltd', 'richardmorales@gmail.com', '09656812427', '2401'], ['Kevin Ashley', 'purple', 'Smith Ltd', 'hmitchell@yahoo.com', '+86(3)7161159375', '1744'], ['Kevin Burns', 'lime', 'Jackson-Harrison', 'joshua56@gmail.com', '1-004-688-3856x1145', '5395']]
        self.assertEqual(filter('example_data.csv', full_name__contains="Kevin"), expected_result)

    def test_when_lt_filter_is_passed(self):
        expected_result = [['Karen Russell', 'purple', 'Ho and Sons', 'morrisjennifer@hotmail.com', '088.899.8659x085', '19'], ['Terry Andrews', 'yellow', 'Wong-Sanchez', 'karenevans@hotmail.com', '(074)820-9740x9897', '15'], ['Karen Ryan', 'blue', 'Johnson-Gray', 'lindsey19@yahoo.com', '1-141-874-1821x0370', '23']]
        self.assertEqual(filter('example_data.csv', salary__lt=150), expected_result)

    def test_when_gt_filter_is_passed(self):
        expected_result = [['Victoria White', 'maroon', 'Nelson-Chavez', 'moralesashley@hotmail.com', '1-343-009-7512x70680', '9938'], ['Timothy Nash', 'silver', 'Valenzuela LLC', 'ygross@hotmail.com', '1-716-425-0834x71436', '9932']]
        self.assertEqual(filter('example_data.csv', salary__gt=9930), expected_result)

    def test_when_order_by_is_passed(self):
        expected_result = [['Timothy Nash', 'silver', 'Valenzuela LLC', 'ygross@hotmail.com', '1-716-425-0834x71436', '9932'], ['Victoria White', 'maroon', 'Nelson-Chavez', 'moralesashley@hotmail.com', '1-343-009-7512x70680', '9938']]
        self.assertEqual(filter('example_data.csv', salary__gt=9930, order_by='full_name'), expected_result)

class TestCount(unittest.TestCase):
    def test_when_filter_not_valid_then_raise_exception(self):
        with self.assertRaises(Exception) as exc:
            count('example_data.csv', name='Diana')
            
    def test_when_one_default_filter_is_passed(self):
        expected_result = 1
        self.assertEqual(count('example_data.csv', full_name='Diana Harris'), expected_result)

    def test_when_more_than_one_default_filters_are_passed(self):
        expected_result = 1
        self.assertEqual(count('example_data.csv',favourite_color="lime", company_name='Martin-Barnes'), expected_result)

    def test_when_startswith_filter_is_passed(self):
        expected_result = 1
        self.assertEqual(count('example_data.csv', full_name__startswith="Diana"), expected_result)

    def test_when_contains_filter_is_passed(self):
        expected_result = 3
        self.assertEqual(count('example_data.csv', full_name__contains="Kevin"), expected_result)

    def test_when_lt_filter_is_passed(self):
        expected_result = 3
        self.assertEqual(count('example_data.csv', salary__lt=150), expected_result)

    def test_when_gt_filter_is_passed(self):
        expected_result = 2
        self.assertEqual(count('example_data.csv', salary__gt=9930), expected_result)

    def test_when_order_by_is_passed(self):
        expected_result = 2
        self.assertEqual(count('example_data.csv', salary__gt=9930, order_by='full_name'), expected_result)


class TestFirst(unittest.TestCase):

    def test_when_order_by_is_not_passed(self):
        expected_result = ['Victoria White', 'maroon', 'Nelson-Chavez', 'moralesashley@hotmail.com', '1-343-009-7512x70680', '9938']
        self.assertEqual(first('example_data.csv', salary__gt=9930), expected_result)

    def test_when_order_by_is_passed(self):
        expected_result = ['Timothy Nash', 'silver', 'Valenzuela LLC', 'ygross@hotmail.com', '1-716-425-0834x71436', '9932']
        self.assertEqual(first('example_data.csv', salary__gt=9930, order_by='full_name'), expected_result)


class TestLast(unittest.TestCase):

    def test_when_order_by_is_not_passed(self):
        expected_result = ['Timothy Nash', 'silver', 'Valenzuela LLC', 'ygross@hotmail.com', '1-716-425-0834x71436', '9932']
        self.assertEqual(last('example_data.csv', salary__gt=9930), expected_result)

    def test_when_order_by_is_passed(self):
        expected_result = ['Victoria White', 'maroon', 'Nelson-Chavez', 'moralesashley@hotmail.com', '1-343-009-7512x70680', '9938']
        self.assertEqual(last('example_data.csv', salary__gt=9930, order_by='full_name'), expected_result)


if __name__ == '__main__':
    unittest.main()