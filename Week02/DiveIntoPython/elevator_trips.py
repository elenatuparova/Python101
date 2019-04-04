def elevator(people_weight, people_floors, max_people, max_weight):
    if len(people_weight) == 0 or len(people_floors) == 0:
        raise Exception('Lists of people\'s weight and people\'s floors must be non empty!')
    trips = 0
    while len(people_weight) > 0:
        current_floors = [people_floors[index] for index, person in enumerate(people_weight)
        if sum(people_weight[:index + 1]) <= max_weight and len(people_weight[:index + 1]) <= max_people]
        trips += len(set(current_floors)) + 1
        people_weight = people_weight[len(current_floors):]
        people_floors = people_floors[len(current_floors):]
    return trips