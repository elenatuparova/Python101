import json
import sys
from random import random
from carracing import Car, Driver, Race, Championship

def set_up_drivers(file_name):
    with open(file_name) as file:
        drivers_data = json.load(file)
    # print(drivers_data)
    drivers = []
    for record in drivers_data['people']:
        new_car = Car(record['car'], record['model'], record['max_speed'])
        new_driver = Driver(record['name'], new_car)
        drivers.append(new_driver)
    return drivers

def main():
    drivers = set_up_drivers('cars.json')
    for driver in drivers:
        print(driver)
    if len(sys.argv) == 1:
        initial_message_to_user = '''Hello PyRacer!
Please, call command with the proper argument:
 $ python3 race.py start <name> <races_count> -> This will start a new championship with the given name, races count and drivers from cars.json
 $ python3 race.py standings -> This will print the standings for each championship that has ever taken place.'''
        print(initial_message_to_user)
    if len(sys.argv) == 4 and sys.argv[1] == 'start':
        new_championship = Championship(sys.argv[2], sys.argv[3])
        for race_num in range(new_championship.races_count):
            new_race = Race(drivers, random())
            new_championship.add_race_to_list(new_race)
            
    if len(sys.argv) == 2 and sys.argv[1] == 'standings':
        pass


if __name__ == '__main__':
    main()