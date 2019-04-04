def list_user_data(all_user_data):
    all_data = ''
    for date in all_user_data.keys():
        all_data += '=== ' + date + ' ===' + '\n'
        for rec_type in all_user_data[date].keys():
            for record in all_user_data[date][rec_type]:
                all_data += str(record[0]) + ', ' + record[1] + ', '
                all_data += 'New Income\n' if rec_type == 'income' else 'New Expense\n'
    print(all_data)


def show_user_incomes(all_user_data):
    incomes = ''
    for date in all_user_data.keys():
        for income in all_user_data[date]['income']:
            if date not in incomes:
                incomes += '=== ' + date + ' ===' + '\n'
            incomes += str(income[0]) + ', ' + income[1] + '\n'
    print(incomes)


def show_user_savings(all_user_data):
    savings = 'Savings:\n'
    for date in all_user_data.keys():
        for rec_type in all_user_data[date].keys():
            for record in all_user_data[date][rec_type]:
                if record[1] == 'Savings':
                    savings += date + ', ' + str(record[0])
                    savings += ', Income\n' if rec_type == 'income' else ', Expense\n'
    print(savings)


def show_user_deposits(all_user_data):
    deposits = 'Deposits:\n'
    for date in all_user_data.keys():
        for rec_type in all_user_data[date].keys():
            for record in all_user_data[date][rec_type]:
                if record[1] == 'Deposit':
                    deposits += date + ', ' + str(record[0])
                    deposits += ', Income\n' if rec_type == 'income' else ', Expense\n'
    print(deposits)


def show_user_expenses(all_user_data):
    expenses = ''
    for date in all_user_data.keys():
        for expense in all_user_data[date]['expense']:
            if date not in expenses:
                expenses += '=== ' + date + ' ===' + '\n'
            expenses += str(expense[0]) + ', ' + expense[1] + '\n'
    print(expenses)


def list_user_expenses_ordered_by_categories(all_user_data):
    expenses = ''
    for date in all_user_data.keys():
        for record in all_user_data[date]['expense']:
            if record[1] not in expenses:
                expenses += record[1] + ':\n'
            expenses += date + ', ' + str(record[0]) + '\n'
    print(expenses)


def show_user_data_per_date(date, all_user_data):
    if date not in all_user_data.keys():
        print('No data for given date!')
        return
    data_on_certain_date = ''
    data_on_certain_date += '=== ' + date + ' ===' + '\n'
    for rec_type in all_user_data[date].keys():
        for record in all_user_data[date][rec_type]:
            data_on_certain_date += str(record[0]) + ', ' + record[1] + ', '
            data_on_certain_date += 'New Income\n' if rec_type == 'income' else 'New Expense\n'
    print(data_on_certain_date)


def list_income_categories(all_user_data):
    income_categories = []
    for date in all_user_data.keys():
        for record in all_user_data[date]['income']:
                income_categories.append(record[1])
    income_categories_unique = set(income_categories)
    income_categories_list = ''
    for income in income_categories_unique:
        income_categories_list += income + '\n'
    print(income_categories_list)


def list_expense_categories(all_user_data):
    expense_categories = []
    for date in all_user_data.keys():
        for record in all_user_data[date]['expense']:
                expense_categories.append(record[1])
    expense_categories_unique = set(expense_categories)
    expense_categories_list = ''
    for expense in expense_categories_unique:
        expense_categories_list += expense + '\n'
    print(expense_categories_list)


def add_income(income_category, money, date, all_user_data):
    if float(money) < 0:
        print('You cannot have negative amount!')
        return
    if date not in all_user_data.keys():
        all_user_data[date] = {'expense': [], 'income': []}
    all_user_data[date]['income'].append((float(money), income_category))
    return all_user_data


def add_expense(expense_category, money, date, all_user_data):
    if float(money) < 0:
        print('You cannot have negative amount!')
        return
    if date not in all_user_data.keys():
        all_user_data[date] = {'expense': [], 'income': []}
    all_user_data[date]['expense'].append((float(money), expense_category))
    return all_user_data


def read_data(file_name):
    file_data = open(file_name)
    all_data_list = file_data.readlines()
    all_user_data = {}
    current_date = ''
    for data in all_data_list:
        if data.startswith('==='):
            current_date = data[4:-5]
            all_user_data[current_date] = {'expense': [], 'income': []}
        else:
            record = data.split(', ')
            if 'Income' in record[2]:
                all_user_data[current_date]['income'].append((float(record[0]), record[1]))
            if 'Expense' in record[2]:
                all_user_data[current_date]['expense'].append((float(record[0]), record[1]))
    return all_user_data

if __name__ == '__main__':
    main()
