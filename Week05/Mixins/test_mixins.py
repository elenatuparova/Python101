from mixins import Jsonable, Xmlable, Panda
import unittest

class TestJsonable(unittest.TestCase):
    def test_when_to_json_then_return_json_representation_of_object(self):
        expected_result = '''{
    "type": "Panda",
    "dict": {
        "name": "Ivo",
        "age": 23,
        "food": "bamboo",
        "weight": 67
    }
}'''
        test_panda = Panda(name='Ivo', age=23, food='bamboo', weight=67)
        self.assertEqual(test_panda.to_json(), expected_result)

    def test_when_from_json_then_instace_object_from_json_string(self):
        test_json_string = '''{
    "type": "Panda",
    "dict": {
        "name": "Tony",
        "age": 23,
        "food": "bamboo",
        "weight": 67
    }
}'''
        expected_result = Panda(name='Tony', age=23, food='bamboo', weight=67)
        self.assertEqual(Panda.from_json(test_json_string), expected_result)

class TestXmlable(unittest.TestCase):
    def test_when_to_xml_then_return_xml_representation_of_object(self):
        expected_result = '<Panda><name>Tony</name><age>23</age><food>bamboo</food><weight>67</weight></Panda>'
        test_panda = Panda(name='Tony', age=23, food='bamboo', weight=67)
        self.assertEqual(test_panda.to_xml(), expected_result)

    def test_when_from_xml_then_instace_object_from_xml_string(self):
        expected_result = Panda(name='Tony', age=23, food='bamboo', weight=67)
        test_xml_string = '<Panda><name>Tony</name><age>23</age><food>bamboo</food><weight>67</weight></Panda>'
        self.assertEqual(Panda.from_xml(test_xml_string), expected_result)

if __name__ == '__main__':
    unittest.main()