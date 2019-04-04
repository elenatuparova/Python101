class Bill:
    def __init__(self, amount):
        if amount < 0:
            raise ValueError('The amount of the bill must be non-negative integer!')
        if not isinstance(amount, int):
            raise TypeError('The amount of the bill must be of type int!')
        self.amount = amount

    def __int__(self):
        return self.amount

    def __str__(self):
        return "A ${0} bill".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.amount == other.amount:
            return True
        return False

    def __hash__(self):
        return hash((self.amount))

class BillBatch:
    def __init__(self, bill_list):
        for bill in bill_list:
            if not isinstance(bill, Bill):
                raise TypeError('Every bill must be an instance of class Bill!')
        self.bills = [bill for bill in bill_list]

    def __len__(self):
        return len(self.bills)

    def __getitem__(self, index):
        return self.bills[index]

    def total(self):
        return sum([int(bill) for bill in self.bills])

class CashDesk:
    def __init__(self):
        self.cash_desk = {}

    def number_of_bills(self):
        number = 0
        for value in self.cash_desk.values():
            number += value
        return number

    def take_money(self, money):
        if isinstance(money, Bill):
            if money not in self.cash_desk.keys():
                self.cash_desk[money] = 0
            self.cash_desk[money] += 1
        elif isinstance(money, BillBatch):
            for bill in money:
                if bill not in self.cash_desk.keys():
                    self.cash_desk[bill] = 0
                self.cash_desk[bill] += 1
        else:
            raise TypeError('Money must be either a single Bill or a BillBatch!')

    def total(self):
        return sum([int(bill)*amount for bill, amount in self.cash_desk.items()])

    def inspect(self):
        str_inspect = ''
        for bill, amount in self.cash_desk.items():
            str_inspect += '$' + str(int(bill)) + ' bills - ' + str(amount) + '\n'
        print(str_inspect)
        return str_inspect
