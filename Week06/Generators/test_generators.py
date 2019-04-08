import unittest
from generators import chain, compress

class TestChain(unittest.TestCase):

    def test_when_both_iterables_are_range(self):
        chained = list(chain(range(0, 4), range(4, 8)))
        expected_result = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(chained, expected_result)

    def test_when_one_iterable_is_list_and_other_is_set(self):
        chained = list(chain([1, 3, 3], {2, 3, 1}))
        expected_result = [1, 3, 3, 1, 2, 3]
        self.assertEqual(chained, expected_result)

    def test_when_both_iterables_are_sets(self):
        chained = list(chain({1, 3, 4}, {2, 5, 6}))
        expected_result = [1, 3, 4, 2, 5, 6]
        self.assertEqual(chained, expected_result)


class TestCompress(unittest.TestCase):

    def test_when_there_is_true_in_mask(self):
        expected_result = ['Panda']
        self.assertEqual(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])), expected_result)

    def test_when_there_is_no_true_in_mask(self):
        expected_result = []
        self.assertEqual(list(compress(["Ivo", "Rado", "Panda"], [False, False, False])), expected_result)

    def test_when_all_values_in_mask_are_true(self):
        expected_result = ['Ivo', 'Rado', 'Panda']
        self.assertEqual(list(compress(["Ivo", "Rado", "Panda"], [True, True, True])), expected_result)


if __name__ == '__main__':
    unittest.main()