from money_tracker import MoneyTracker

class Menu:

    @classmethod
    def choose_option(cls, money_tracker):
        if not isinstance(money_tracker, MoneyTracker):
            raise TypeError('Options must be chosen for an instance of class MoneyTracker!')
        initital_message_to_user = '''Choose one of the following options to continue:
        1 - show all data
        2 - show data for specific date
        3 - show incomes
        4 - show savings
        5 - show deposits
        6 - show expenses
        7 - show expenses, ordered by type
        8 - list income types
        9 - list expense types
        10 - add new income
        11 - add new expense
        12 - exit
        '''
        command = input(initital_message_to_user)
        while True:
            if command not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
                print('Invalid option! Try again!')
            if command == '1':
                money_tracker.list_user_data()
            if command == '2':
                date = input('Date (in format dd-mm-yyyy):\n')
                money_tracker.show_user_data_per_date(date)
            if command == '3':
                money_tracker.show_user_incomes()
            if command == '4':
                money_tracker.show_user_savings()
            if command == '5':
                money_tracker.show_user_deposits()
            if command == '6':
                money_tracker.show_user_expenses()
            if command == '7':
                money_tracker.list_user_expenses_ordered_by_record_type()
            if command == '8':
                money_tracker.list_income_types()
            if command == '9':
                money_tracker.list_expense_types()
            if command == '10':
                amount = input('New income amount:\n')
                record_type = input('New income type:\n')
                date = input('New income date:\n')
                money_tracker.add_income(amount, record_type, date)
            if command == '11':
                amount = input('New expense amount:\n')
                record_type = input('New expense type:\n')
                date = input('New expense date:\n')
                money_tracker.add_expense(amount, record_type, date)
            if command == '12':
                break
            command = input(initital_message_to_user)