class Category:
    def __init__(self, amount, record_type, date):
        if not isinstance(amount, float):
            raise TypeError('Amount must be of type float!')
        if amount < 0:
            raise ValueError('Amount must be non-negative!')
        self._amount = amount
        if not isinstance(record_type, str):
            raise TypeError('Record type must be of type string!')
        self._record_type = record_type
        if not isinstance(date, str):
            raise TypeError('Date must be of type string!')
        self._date = date

    @property
    def amount(self):
        return self._amount

    @property
    def record_type(self):
        return self._record_type

    @property
    def date(self):
        return self._date

    def __str__(self):
        return str(self._amount) + ', ' + str(self._record_type)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(str(_amount) + str(_record_type) + str(_date))

class Income(Category):
    _category = 'Income'

    def __init__(self, amount, record_type, date):
        super().__init__(amount, record_type, date)

    @property
    def category(cls):
        return cls._category

    def __str__(self):
        return super().__str__() + ', New Income'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(str(_amount) + str(_record_type) + str(_date) + str(_category))


class Expense(Category):
    _category = 'Expense'

    def __init__(self, amount, type, date):
        super().__init__(amount, type, date)

    @property
    def category(cls):
        return cls._category

    def __str__(self):
        return super().__str__() + ', New Expense'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(str(_amount) + str(_record_type) + str(_date) + str(_category))