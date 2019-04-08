import unittest
from category import Category, Income, Expense
from parse_money_tracker_data import Parser
from aggregated_money_tracker import AggregatedMoneyTracker
from money_tracker import MoneyTracker
from money_tracker_menu import Menu

class TestCategory(unittest.TestCase):

    def test_init_when_amount_is_not_float_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Category('320.5', 'Salary', '23-12-2018')

    def test_init_when_amount_is_negative_then_raise_value_error(self):
        with self.assertRaises(ValueError):
            Category(-320.5, 'Salary', '23-12-2018')

    def test_init_when_record_type_is_not_str_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Category(320.5, True, '23-12-2018')

    def test_init_when_date_is_not_str_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Category(320.5, 'Salary', 23)

    def test_when_amount_then_return_amount(self):
        test_category = Category(320.5, 'Salary', '23-12-2018')
        expected_result = 320.5
        self.assertEqual(test_category.amount, expected_result)

    def test_when_record_type_then_return_record_type(self):
        test_category = Category(320.5, 'Salary', '23-12-2018')
        expected_result = 'Salary'
        self.assertEqual(test_category.record_type, expected_result)

    def test_when_date_then_return_date(self):
        test_category = Category(320.5, 'Salary', '23-12-2018')
        expected_result = '23-12-2018'
        self.assertEqual(test_category.date, expected_result)

    def test_str_dunder(self):
        test_category = Category(320.5, 'Salary', '23-12-2018')
        expected_result = '320.5, Salary'
        self.assertEqual(str(test_category), expected_result)

    def test_eq_dunder_when_two_categories_are_equal(self):
        test_category1 = Category(320.5, 'Salary', '23-12-2018')
        test_category2 = Category(320.5, 'Salary', '23-12-2018')
        self.assertTrue(test_category1 == test_category2)

    def test_eq_dunder_when_two_categories_are_not_equal(self):
        test_category1 = Category(320.5, 'Salary', '23-12-2018')
        test_category2 = Category(320.5, 'Salary', '23-11-2018')
        self.assertFalse(test_category1 == test_category2)


class TestIncome(unittest.TestCase):

    def test_when_category_then_return_category_cls_attribute(self):
        test_income = Income(320.5, 'Salary', '23-12-2018')
        expected_result = 'Income'
        self.assertEqual(test_income.category, expected_result)

    def test_str_dunder(self):
        test_income = Income(320.5, 'Salary', '23-12-2018')
        expected_result = '320.5, Salary, New Income'
        self.assertEqual(str(test_income), expected_result)

    def test_eq_dunder_when_two_incomes_are_equal(self):
        test_income1 = Income(320.5, 'Salary', '23-12-2018')
        test_income2 = Income(320.5, 'Salary', '23-12-2018')
        self.assertTrue(test_income1 == test_income2)

    def test_eq_dunder_when_two_incomes_are_not_equal(self):
        test_income1 = Income(320.5, 'Salary', '23-12-2018')
        test_income2 = Income(320.5, 'Salary', '23-11-2018')
        self.assertFalse(test_income1 == test_income2)


class TestExpense(unittest.TestCase):

    def test_when_category_then_return_category_cls_attribute(self):
        test_expense = Expense(40.6, 'Clothes', '23-12-2018')
        expected_result = 'Expense'
        self.assertEqual(test_expense.category, expected_result)

    def test_str_dunder(self):
        test_expense = Expense(40.6, 'Clothes', '23-12-2018')
        expected_result = '40.6, Clothes, New Expense'
        self.assertEqual(str(test_expense), expected_result)

    def test_eq_dunder_when_two_expenses_are_equal(self):
        test_expense1 = Expense(40.6, 'Clothes', '23-12-2018')
        test_expense2 = Expense(40.6, 'Clothes', '23-12-2018')
        self.assertTrue(test_expense1 == test_expense2)

    def test_eq_dunder_when_two_expenses_are_not_equal(self):
        test_expense1 = Expense(40.6, 'Clothes', '23-12-2018')
        test_expense2 = Expense(40.6, 'Clothes', '23-11-2018')
        self.assertFalse(test_expense1 == test_expense2)


class TestParser(unittest.TestCase):

    def test_when_parsing_then_return_list_of_lines(self):
        expected_result = ['=== 22-03-2019 ===\n', '760, Salary, New Income\n', '5.5, Eating Out, New Expense\n', '34, Clothes, New Expense\n', '41.79, Food, New Expense\n', '12, Eating Out, New Expense\n', '7, House, New Expense\n', '14, Pets, New Expense\n', '112.40, Bills, New Expense\n', '21.5, Transport, New Expense\n', '=== 23-03-2019 ===\n', '50, Savings, New Income\n', '15, Food, New Expense\n', '200, Deposit, New Income\n', '5, Sports, New Expense']
        self.assertEqual(Parser.parse_money_tracker_data('money_tracker.txt'), expected_result)


class TestAggregatedMoneyTracker(unittest.TestCase):

    def test_when_init_then_make_parsed_lines_into_a_dictionary(self):
        test_aggregated = AggregatedMoneyTracker('money_tracker.txt')
        expected_result = {'22-03-2019': {'Expenses': [Expense(5.5, 'Eating Out', '22-03-2019'), Expense(34.0, 'Clothes', '22-03-2019'), Expense(41.79, 'Food', '22-03-2019'), Expense(12.0, 'Eating Out', '22-03-2019'), Expense(7.0, 'House', '22-03-2019'), Expense(14.0, 'Pets', '22-03-2019'), Expense(112.4, 'Bills', '22-03-2019'), Expense(21.5, 'Transport', '22-03-2019')], 'Incomes': [Income(760.0, 'Salary', '22-03-2019')]}, '23-03-2019': {'Expenses': [Expense(15.0, 'Food', '23-03-2019'), Expense(5.0, 'Sports', '23-03-2019')], 'Incomes': [Income(50.0, 'Savings', '23-03-2019'), Income(200.0, 'Deposit', '23-03-2019')]}}
        self.assertEqual(test_aggregated.records, expected_result)

    def test_len_dunder_return_number_of_records(self):
        test_aggregated = AggregatedMoneyTracker('money_tracker.txt')
        expected_result = 13
        self.assertEqual(len(test_aggregated), expected_result)

    # def test_str_dunder(self):
#         test_aggregated = AggregatedMoneyTracker('money_tracker.txt')
#         expected_result = '''=== 22-03-2019 ===
# 760, Salary, New Income
# 5.5, Eating Out, New Expense
# 34, Clothes, New Expense
# 41.79, Food, New Expense
# 12, Eating Out, New Expense
# 7, House, New Expense
# 14, Pets, New Expense
# 112.40, Bills, New Expense
# 21.5, Transport, New Expense
# === 23-03-2019 ===
# 50, Savings, New Income
# 15, Food, New Expense
# 200, Deposit, New Income
# 5, Sports, New Expense
# '''
#         self.assertEqual(str(test_aggregated), expected_result)


class TestMoneyTracker(unittest.TestCase):

    def test_init_when_passed_non_aggregated_money_tracker_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            MoneyTracker('money_tracker.txt')

    def test_len_dunder_return_number_of_records(self):
        test_money_tracker = MoneyTracker(AggregatedMoneyTracker('money_tracker.txt'))
        expected_result = 13
        self.assertEqual(len(test_money_tracker), expected_result)

if __name__ == '__main__':
    unittest.main()