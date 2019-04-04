from money_tracker import *

def main():
    file_name = 'money_tracker.txt'
    try:
        all_user_data = read_data(file_name)
    except (OSError, IOError):
        print('Invalid file name! File not found!')
    else:
        initital_message_to_user = 'Choose one of the following options to continue:\n1 - show all data\n2 - show data for specific date\n3 - show expenses, ordered by categories\n4 - add new income\n5 - add new expense\n6 - exit\n'
        command = input(initital_message_to_user)
        while True:
            if command not in ['1', '2', '3', '4', '5', '6']:
                print('Invalid option! Try again!')
            if command == '1':
                list_user_data(all_user_data)
            if command == '2':
                date = input('Date (in format dd-mm-yyyy):\n')
                show_user_data_per_date(date, all_user_data)
            if command == '3':
                list_user_expenses_ordered_by_categories(all_user_data)
            if command == '4':
                money = input('New income amount:\n')
                income_category = input('New income type:\n')
                date = input('New income date:\n')
                add_income(income_category, money, date, all_user_data)
            if command == '5':
                money = input('New expense amount:\n')
                income_category = input('New expense type:\n')
                date = input('New expense date:\n')
                add_expense(income_category, money, date, all_user_data)
            if command == '6':
                break
            command = input(initital_message_to_user)

if __name__ == '__main__':
    main()