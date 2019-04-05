from random import sample
import json
import os

class Car:
    def __init__(self, car, model, max_speed):
        if not isinstance(car, str):
            raise TypeError('Car must be of type string!')
        self.car = car
        if not isinstance(model, str):
            raise TypeError('Model must be of type string!')
        self.model = model
        if not isinstance(max_speed, int):
            raise TypeError('Max speed must be of type int!')
        self.max_speed = max_speed

    def __str__(self):
        return "Car: {0}".format(self.car) + "\nModel: {0}".format(self.model) + "\nMax speed: {0}".format(self.max_speed) + '\n'

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.car + self.model))

class Driver:
    def __init__(self, name, car):
        if not isinstance(name, str):
            raise TypeError('Name of driver must be of type string!')
        self.name = name
        if not isinstance(car, Car):
            raise TypeError('Car must be an instance of class Car!')
        self.car = car

    def __str__(self):
        return "Name: {0}".format(self.name) + '\n' + str(self.car)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.name))

class Race:
    def __init__(self, drivers, crash_chance, championship, race_number):
        if not isinstance(drivers, list):
            raise TypeError('Drivers must be in a list!')
        for driver in drivers:
            if not isinstance(driver, Driver):
                raise TypeError('Every driver must be an instance of class Driver!')
        self.drivers = [driver for driver in drivers]
        if not isinstance(crash_chance, float):
            raise TypeError('Crash chance must be float!')
        if crash_chance < 0 or crash_chance > 1:
            raise ValueError('Crash chance must be a number between 0 and 1!')
        self.crash_chance = crash_chance
        if not isinstance(championship, str):
            raise TypeError('Championship name must be string!')
        self.championship = championship
        if not isinstance(race_number, int):
            raise TypeError('Number of race must be integer!')
        self.race_number = race_number
        self.results = {driver.name: 0 for driver in self.drivers}

    def __str__(self):
        str_race = ''
        for index, driver in enumerate(self.drivers):
            str_race += 'Driver #' + str(index + 1) + ':\n' + str(driver)
        str_race += 'Crash chance: {0}'.format(self.crash_chance) + '\n'
        return str_race

    def __repr__(self):
        return self.__str__()

    def run_race(self):
        crashes_num = round(self.crash_chance*len(self.drivers))
        self.crashed_drivers = sample(self.drivers, k = crashes_num)
        remaining_drivers = [driver for driver in self.drivers if driver not in self.crashed_drivers]
        if len(self.drivers) - crashes_num >= 3:
            ranking = sample(remaining_drivers, k = 3)
        elif len(self.drivers) - crashes_num == 0:
            ranking = []
        else:
            ranking = sample(remaining_drivers, k = len(self.drivers) - crashes_num)
        current_points = 8
        for driver in ranking:
            self.results[driver.name] += current_points
            current_points -= 4


    # def save_results(self):
    #     with open('results.json', 'w') as results:
    #         results.seek(0)
    #         first_char = results.read(1)
    #         if first_char:
    #             current_results = json.load(results)
    #         else:
    #             current_results = {}
    #         print(current_results)
    #         if not self.championship in current_results.keys():
    #             current_results[self.championship] = {'races': []}
    #         current_results[self.championship]['races'].append({'race': self.race_number, 'results': self.results, 'crashed': [driver.name for driver in self.crashed_drivers]})
    #         json.dump(current_results, results, indent=4)


class Championship:
    def __init__(self, name, races_count):
        if not isinstance(name, str):
            raise TypeError('Name of race must be of type string!')
        self.name = name
        if not isinstance(races_count, int):
            raise TypeError('Number of races must be integer!')
        if races_count <= 0:
            raise ValueError('Number of races must be a positive number!')
        self.races_count = races_count
        self.ranking = {}
        self.races_list = []

    def __hash__(self):
        return hash(self.name)

    def add_race_to_list(self, race):
        if not isinstance(race, Race):
            raise TypeError('Race must be an instance of class Race!')
        self.races_list.append(race)

    def run_races(self):
        for race in self.races_list:
            race.run_race()

    def top3(self):
        pass