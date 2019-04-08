from parse_money_tracker_data import Parser
from category import Category, Income, Expense

class AggregatedMoneyTracker:
    def __init__(self, file_name):
        self.records = {}
        data = Parser.parse_money_tracker_data(file_name)
        for line in data:
            if line.startswith('==='):
                current_date = line[4:-5]
                self.records[current_date] = {'Expenses': [], 'Incomes': []}
            else:
                record = line.split(', ')
                if 'Income' in record[2]:
                    self.records[current_date]['Incomes'].append(Income(float(record[0]), record[1], current_date))
                if 'Expense' in record[2]:
                    self.records[current_date]['Expenses'].append(Expense(float(record[0]), record[1], current_date))

    def __len__(self):
        number_of_records = 0
        for date in self.records.keys():
            for category in self.records[date].keys():
                number_of_records += len(self.records[date][category])
        return number_of_records

    def __str__(self):
        str_repr = ''
        for date in self.records.keys():
            str_repr += '=== ' + date + ' ===' + '\n'
            for category in self.records[date].keys():
                for record in self.records[date][category]:
                    str_repr += str(record.amount) + ', ' + record.record_type + ', New' + type(record).__name__ + '\n'
        return str_repr

    def __repr__(self):
        return self.__str__