import sys
import json

def business_card(person):
    file_name = person['first_name'].lower() + '_' + person['last_name'].lower() + '.html'
    file = open(file_name, 'w')
    file_content = '''<!DOCTYPE html>
    <html>
    <head>
        <title>''' + person['first_name'] + ' ' + person['last_name'] + '''</title>
        <link rel="stylesheet" type="text/css" href="styles.css">
    </head>
    <body>
        <div class="business-card ''' + person['gender'] + '''">
            <h1 class="full-name">''' + person['first_name'] + ' ' + person['last_name'] + '''</h1>
            <img class="avatar" src="avatars/''' + person['avatar'] + '''">
            <div class="base-info">
                <p>Age: ''' + str(person['age']) + '''</p>
                <p>Birth date: ''' + person['birth_date'] + '''</p>
                <p>Birth place: ''' + person['birth_place'] + '''</p>
                <p>Gender: ''' + person['gender'] + '''</p>
            </div>
            <div class="interests">
                <h2>Interests:</h2>
                    <ul>'''
    for interest in person['interests']:
        file_content += '\n\t\t\t<li>' + interest + '</li>'
    file_content += '''
                    </ul>
            </div>
            <div class="skills">
                <h2>Skills:</h2>
                    <ul>'''
    for skill in person['skills']:
        file_content += '\n\t\t\t<li>' + skill['name'] + ' - ' + str(skill['level']) + '</li>'
    file_content += '''
                    </ul>
            </div>
        </div>  
    </body>
    </html>'''
    file.write(file_content)
    file.close()
    return file_name

def main(filename):
    with open(filename) as file:
        data = json.load(file)
    business_cards = []
    for person in data['people']:
        business_cards.append(business_card(person))
    return business_cards

if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)