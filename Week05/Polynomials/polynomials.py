import sys

class Monomials:
    def __init__(self, monomial):
        if '*' in monomial and '^' in monomial:
            self._coefficient = int(monomial.split('*')[0])
            self._power_of_variable = int(monomial.split('^')[1])
        elif '*' in monomial and '^' not in monomial:
            self._coefficient = int(monomial.split('*')[0])
            self._power_of_variable = 1
        elif '*' not in monomial and '^' in monomial:
            self._coefficient = 1
            self._power_of_variable = int(monomial.split('^')[1])
        elif '*' not in monomial and '^' in monomial and 'x' in monomial:
            self._coefficient = 1
            self._power_of_variable = 1
        else:
            self._coefficient = int(monomial)
            self._power_of_variable = 0
        self._str_monomial = monomial.strip()

    @property
    def coefficient(self):
        return self._coefficient

    @property
    def power_of_variable(self):
        return self._power_of_variable
    
    def __str__(self):
        return self._str_monomial

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if self._power_of_variable == other._power_of_variable:
            added_coefficient = self._coefficient + other._coefficient
            if self._power_of_variable == 0:
                return Monomials(str(added_coefficient))
            if self._power_of_variable == 1:
                return Monomials('{}*x'.format(added_coefficient))
            if self._power_of_variable > 1:
                return Monomials('{}*x^{}'.format(added_coefficient, self._power_of_variable))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def calculate_derivative(self):
        if self._power_of_variable == 0:
            return '0'

        if self._power_of_variable == 1:
            return str(self._coefficient)

        derivative_coefficient = self._coefficient * self._power_of_variable
        derivative_power_of_variable = self._power_of_variable - 1

        if derivative_coefficient > 1 and derivative_power_of_variable == 1:
            return '{}*x'.format(str(derivative_coefficient))

        if derivative_coefficient > 1 and derivative_power_of_variable > 1:
            return '{}*x^{}'.format(str(derivative_coefficient), str(derivative_power_of_variable))


class Polynomials:
    def __init__(self, polynomial):
        str_monomials = polynomial.split('+')
        monomials = [Monomials(monomial) for monomial in str_monomials]
        monomials.sort(key=lambda monomial: monomial.power_of_variable, reverse=True)
        self._monomials = [monomials[0]]
        current_index = 0
        if len(monomials) > 1:
            for index in range(1, len(monomials)):
                if self._monomials[current_index].power_of_variable == monomials[index].power_of_variable:
                    self._monomials[current_index] += monomials[index]
                else:
                    current_index += 1
                    self._monomials.append(monomials[index])

    @property
    def monomials(self):
        return self._monomials

    def __str__(self):
        str_polynomial = ''
        for index in range(len(self._monomials)):
            str_polynomial += str(self._monomials[index]) + ' + '
        return str_polynomial.strip(' + ')

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def calculate_derivative(self):
        if len(self._monomials) == 1:
            return self._monomials[0].calculate_derivative()

        derivatives = [monomial.calculate_derivative() for monomial in self._monomials]
        polynomial_derivative = ''
        for index in range(len(derivatives) - 1):
            polynomial_derivative += str(derivatives[index]) + ' + '

        if derivatives[len(derivatives) - 1] != '0':
            return polynomial_derivative + str(derivatives[len(derivatives) - 1])

        return polynomial_derivative.strip(' + ')


def main():
    polynomial = Polynomials(sys.argv[1])
    print('Derivative of f(x) = ' + str(polynomial) + ' is:')
    print('f\'(x) = ' + polynomial.calculate_derivative())

if __name__ == '__main__':
    main()