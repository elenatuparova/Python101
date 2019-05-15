from sql_actions import *

def main():
    command = input('''Hello! This is your business card catalog. What would you like? (enter "help" to list all available options)
>>> Enter command: ''')

    while command != 'exit':
        if command == 'add':
            user_name = input('Enter username: ')
            email = input('Enter email: ')
            age = input('Enter age: ')
            phone = input('Enter phone: ')
            additional_info = input('Enter additional info: ')
            add_user(user_name, email, int(age), phone, additional_info)

        elif command == 'list':
            print('''#############
###Contacts###
#############

''')
            all_users = list_users()
            for idx, user in enumerate(all_users):
                print('{idx}. ID: {id}, Email: {email}, Full name: {full_name}'. format(idx=idx + 1, id=user[0], email=user[2], full_name=user[1]))

        elif command == 'get':
            uid = input('Enter ID: ')
            user = get_user(uid)
            if len(user) != 0:
                print('''Contact info:

###############
ID: {id},
Full name: {full_name}
Email: {email}
Age: {age}
Phone: {phone}
Additional info: {additional_info}
##############
'''.format(id=user[0], full_name=user[1], email=user[2], age=user[3], phone=user[4], additional_info=user[5]))
            else:
                print('There is no user with such ID!')

        elif command == 'delete':
            uid = input('Enter ID: ')
            user = delete_user(uid)
            if len(user) != 0:
                print('''Following contact is deleted successfully:

###############
ID: {id},
Full name: {full_name}
Email: {email}
Age: {age}
Phone: {phone}
Additional info: {additional_info}
##############
'''.format(id=user[0], full_name=user[1], email=user[2], age=user[3], phone=user[4], additional_info=user[5]))
            else:
                print('There is no user with such ID!')

        elif command == 'help':
            print('''#############
###Options###
#############

1. `add` - insert new business card
2. `list` - list all business cards
3. `delete` - delete a certain business card (`ID` is required)
4. `get` - display full information for a certain business card (`ID` is required)
5. `help` - list all available options
6. `exit` - exit the catalog
''')

        elif command == 'exit':
            break

        else:
            print('Invalid option! Enter "help" to list all available options!')

        command = input('>>> Enter command: ')

if __name__ == '__main__':
    main()