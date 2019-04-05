import unittest
from carracing import Car, Driver, Race, Championship

class TestCar(unittest.TestCase):

    def test_init_when_car_is_not_str_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Car(False, 'Astra', 240)

    def test_init_when_model_is_not_str_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Car('Opel', 3, 240)

    def test_init_when_max_speed_is_not_str_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Car('Opel', 'Astra', '240')

    def test_str_dunder(self):
        test_car = Car('Opel', 'Astra', 240)
        expected_result = 'Car: Opel\nModel: Astra\nMax speed: 240\n'
        self.assertEqual(str(test_car), expected_result)

class TestDriver(unittest.TestCase):

    def test_init_when_driver_is_not_str_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Driver(34, Car('Opel', 'Astra', 240))

    def test_init_when_car_is_not_of_class_car_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Driver('Ivo', ('Opel', 'Astra', 240))
    
    def test_str_dunder(self):
        test_driver = Driver('Ivo', Car('Opel', 'Astra', 240))
        expected_result = 'Name: Ivo\nCar: Opel\nModel: Astra\nMax speed: 240\n'
        self.assertEqual(str(test_driver), expected_result)

class TestRace(unittest.TestCase):
    
    def test_init_when_drivers_is_not_list_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Race((Driver('Ivo', Car('Opel', 'Astra', 240)), Driver('Rado', Car('Pegeout', '107', 180))), 0.5, 'Pandarace', 3)

    def test_init_when_one_of_drivers_is_not_of_class_car_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Race([Driver('Ivo', Car('Opel', 'Astra', 240)), ('Rado', Car('Pegeout', '107', 180))], 0.5, 'Pandarace', 3)

    def test_init_when_crash_chance_is_not_float_then_raise_type_error(self):
        with self.assertRaises(TypeError):
            Race([Driver('Ivo', Car('Opel', 'Astra', 240)), Driver('Rado', Car('Pegeout', '107', 180))], '0.5', 'Pandarace', 3)

    def test_init_when_crash_chance_is_not_float_then_raise_value_error(self):
        with self.assertRaises(ValueError):
            Race([Driver('Ivo', Car('Opel', 'Astra', 240)), Driver('Rado', Car('Pegeout', '107', 180))], 1.5, 'Pandarace', 3)

    def test_init_when_championship_name_is_not_str_then_return_type_error(self):
        with self.assertRaises(TypeError):
            Race([Driver('Ivo', Car('Opel', 'Astra', 240)), Driver('Rado', Car('Pegeout', '107', 180))], 0.5, 12, 3)

    def test_init_when_race_number_is_not_int_then_return_type_error(self):
        with self.assertRaises(TypeError):
            Race([Driver('Ivo', Car('Opel', 'Astra', 240)), Driver('Rado', Car('Pegeout', '107', 180))], 0.5, 'Pandarace', '3')


class TestChampionship(unittest.TestCase):

    def test_init_when_championship_name_is_not_str_then_return_type_error(self):
        with self.assertRaises(TypeError):
            Championship(3, 3)

    def test_init_when_races_count_is_not_int_then_return_type_error(self):
        with self.assertRaises(TypeError):
            Championship('Pandarace', '3')

    def test_init_when_races_count_is_non_positive_then_return_value_error(self):
        with self.assertRaises(ValueError):
            Championship('Pandarace', -3)

if __name__ == '__main__':
    unittest.main()