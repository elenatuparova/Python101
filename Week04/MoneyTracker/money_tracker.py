from category import Category, Income, Expense
from aggregated_money_tracker import AggregatedMoneyTracker

class MoneyTracker:

    def __init__(self, aggregated_data):
        if not isinstance(aggregated_data, AggregatedMoneyTracker):
            raise TypeError('Attribute must be an instance of class AggregatedMoneyTracker!')
        self.aggregated_data = aggregated_data

    def __len__(self):
        return len(self.aggregated_data)

    def __str__(self):
        return str(self.aggregated_data)

    def __repr__(self):
        return self.__str__

    def list_user_data(self):
        print(self)

    def show_user_incomes(self):
        incomes = ''
        for date in self.aggregated_data.records.keys():
            for income in self.aggregated_data.records[date]['Incomes']:
                if date not in incomes:
                    incomes += '=== ' + date + ' ===' + '\n'
                incomes += str(income.amount) + ', ' + income.record_type + '\n'
        print(incomes)
        return incomes

    def show_user_savings(self):
        savings = 'Savings:\n'
        for date in self.aggregated_data.records.keys():
            for category in self.aggregated_data.records[date].keys():
                for record in self.aggregated_data.records[date][category]:
                    if record.record_type == 'Savings':
                        savings += date + ', ' + str(record.amount) + type(record).__name__ + '\n'
        print(savings)
        return savings

    def show_user_deposits(self):
        deposits = 'Deposits:\n'
        for date in self.aggregated_data.records.keys():
            for category in self.aggregated_data.records[date].keys():
                for record in self.aggregated_data.records[date][category]:
                    if record.record_type == 'Deposit':
                        deposits += str(record) + '\n'
        print(deposits)
        return deposits

    def show_user_expenses(self):
        expenses = ''
        for date in self.aggregated_data.records.keys():
            for expense in self.aggregated_data.records[date]['Expenses']:
                if date not in expenses:
                    expenses += '=== ' + date + ' ===' + '\n'
                expenses += str(expense) + '\n'
        print(expenses)
        return expenses

    def list_user_expenses_ordered_by_record_type(self):
        expenses = ''
        for date in self.aggregated_data.records.keys():
            for record in self.aggregated_data.records[date]['Expenses']:
                if record.record_type not in expenses:
                    expenses += record.record_type + ':\n'
                expenses += date + ', ' + str(record.amount) + '\n'
        print(expenses)
        return expenses

    def show_user_data_per_date(self, date):
        if date not in self.aggregated_data.records.keys():
            print('No data for given date!')
            return
        data_on_certain_date = ''
        data_on_certain_date += '=== ' + date + ' ===' + '\n'
        for category in self.aggregated_data.records[date].keys():
            for record in self.aggregated_data.records[date][category]:
                data_on_certain_date += str(record) + '\n'
        print(data_on_certain_date)
        return data_on_certain_date

    def list_income_types(self):
        income_types_list = []
        for date in self.aggregated_data.records.keys():
            for record in self.aggregated_data.records[date]['Incomes']:
                    income_types_list.append(record.record_type)
        income_types = ''
        for income in set(income_types_list):
            income_types += income + '\n'
        print(income_types)
        return income_types

    def list_expense_types(self):
        expense_types_list = []
        for date in self.aggregated_data.records.keys():
            for record in self.aggregated_data.records[date]['Expenses']:
                    expense_types_list.append(record.record_type)
        expense_types = ''
        for expense in set(expense_types_list):
            expense_types += expense + '\n'
        print(expense_types)
        return expense_types

    def add_income(self, amount, record_type, date):
        if date not in self.aggregated_data.records.keys():
            self.aggregated_data.records[date] = {'Expenses': [], 'Incomes': []}
        self.aggregated_data.records[date]['Incomes'].append(Income(float(amount), record_type, date))

    def add_expense(self, amount, record_type, date):
        if date not in self.aggregated_data.records.keys():
            self.aggregated_data.records[date] = {'Expenses': [], 'Incomes': []}
        self.aggregated_data.records[date]['Expenses'].append(Expense(float(amount), record_type, date))