import unittest
from cashdesk import Bill, BillBatch, CashDesk

class TestBill(unittest.TestCase):

    def test_when_amount_is_negative_then_raise_value_error(self):
        with self.assertRaises(ValueError):
            Bill(-10)

    def test_when_amount_is_not_int_then_raise_value_error(self):
        with self.assertRaises(TypeError):
            Bill('10')

    def test_int_dunder(self):
        test_bill = Bill(10)
        expected_result = 10
        self.assertEqual(int(test_bill), expected_result)

    def test_str_dunder(self):
        test_bill = Bill(10)
        expected_result = 'A $10 bill'
        self.assertEqual(str(test_bill), expected_result)

    def test_eq_dunder_when_two_bills_have_same_value_then_return_true(self):
        test_bill1 = Bill(10)
        test_bill2 = Bill(10)
        self.assertTrue(test_bill1 == test_bill2)

    def test_eq_dunder_when_two_bills_have_different_values_then_return_false(self):
        test_bill1 = Bill(10)
        test_bill2 = Bill(20)
        self.assertFalse(test_bill1 == test_bill2)

class TestBillBatch(unittest.TestCase):

    def test_when_one_of_items_in_list_is_not_bill_then_return_type_error(self):
        with self.assertRaises(TypeError):
            BillBatch('10')

    def test_len_dunder(self):
        test_billbatch = BillBatch([Bill(10), Bill(20)])
        expected_result = 2
        self.assertEqual(len(test_billbatch), expected_result)

    def test_when_total_then_return_sum_of_amounts_of_all_bills_in_billbatch(self):
        test_billbatch = BillBatch([Bill(10), Bill(20)])
        expected_result = 30
        self.assertEqual(test_billbatch.total(), expected_result)

class TestCashDesk(unittest.TestCase):

    def test_take_money_when_a_billbatch_is_added(self):
        test_cashdesk = CashDesk()
        test_cashdesk.take_money(BillBatch([Bill(10), Bill(10), Bill(20)]))
        expected_result = 3
        self.assertEqual(test_cashdesk.number_of_bills(), expected_result)

    def test_take_money_when_single_bill_is_added(self):
        test_cashdesk = CashDesk()
        test_cashdesk.take_money(Bill(10))
        expected_result = 1
        self.assertEqual(test_cashdesk.number_of_bills(), expected_result)

    def test_take_money_when_one_of_items_in_list_is_not_bill_then_return_type_error(self):
        with self.assertRaises(TypeError):
            test_cashdesk = CashDesk()
            test_cashdesk.take_money(10)

    def test_when_total_then_return_sum_of_amounts_of_all_bills_in_cashdesk(self):
        test_cashdesk = CashDesk()
        test_cashdesk.take_money(BillBatch([Bill(10), Bill(10), Bill(20)]))
        expected_result = 40
        self.assertEqual(test_cashdesk.total(), expected_result)

    def test_when_inspect_then_print_table_repr_of_cash_desk(self):
        test_cashdesk = CashDesk()
        test_cashdesk.take_money(BillBatch([Bill(10), Bill(10), Bill(20)]))
        expected_result = '$10 bills - 2\n$20 bills - 1\n'
        self.assertEqual(test_cashdesk.inspect(), expected_result)

if __name__ == '__main__':
    unittest.main()