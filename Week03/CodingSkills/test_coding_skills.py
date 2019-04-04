import unittest
from coding_skills import coding_skills

class TestCodingSkills(unittest.TestCase):

    def test_coding_skills(self):
        expected_result = '''C++: Cherna Ninja
PHP: Rado Rado
Python: Ivo Ivo
C#: Pavli Pavli
Haskell: Rado Rado
Java: Rado Rado
JavaScript: Rosi Rosi
Ruby: Rosi Rosi
CSS: Pavli Pavli
C: Cherna Ninja
'''
        self.assertEqual(coding_skills('data.json'), expected_result)

if __name__ == '__main__':
    unittest.main()