import unittest
from business_cards import *

class TestBusinessCards(unittest.TestCase):

    def test_if_returns_correct_names_of_files(self):
        test_person = {'first_name': 'Cherna', 'last_name': 'Ninja', 'age': 100, 'birth_date': '10/10/2100', 'birth_place': 'Tokyo', 'gender': 'ninja', 'interests': ['fighting'], 'avatar': 'do-i-exist.png', 'skills': [{'name': 'C++', 'level': 99}, {'name': 'C', 'level': 99}]}
        expected_result = 'cherna_ninja.html'
        self.assertEqual(business_card(test_person), expected_result)


if __name__ == '__main__':
    unittest.main()