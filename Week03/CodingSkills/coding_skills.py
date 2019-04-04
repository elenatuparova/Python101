import sys
import json

def coding_skills(file_name):
    with open(file_name) as file:
        data = json.load(file)
    max_skills = {}
    for person in data['people']:
        for skill in person['skills']:
            if skill['name'] not in max_skills.keys():
                max_skills[skill['name']] = {'person': person['first_name'] + ' ' + person['last_name'], 'level': skill['level']}
            if skill['level'] > max_skills[skill['name']]['level']:
                max_skills[skill['name']] = {'person': person['first_name'] + ' ' + person['last_name'], 'level': skill['level']}
    skill_output = ''
    for skill in max_skills.keys():
        skill_output += skill + ': ' + max_skills[skill]['person'] + '\n'
    print(skill_output)

def main():
    arguments = sys.argv
    coding_skills(arguments[1])

if __name__ == '__main__':
    main()