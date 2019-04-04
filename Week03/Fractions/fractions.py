from math import sqrt

def is_prime(num):
    is_prime = True
    for divisor in range (2, num):
        if num % divisor == 0 and divisor != num:
            is_prime = False
            break
    return is_prime

def generate_primes(upperbound):
    primes = [1]
    for num in range(2, upperbound):
        if is_prime(num):
            primes.append(num)
    return primes

def simplify_fraction(fraction):
    if not isinstance(fraction, tuple):
        raise Exception('You should enter a tuple!')

    nominator = fraction[0]
    denominator = fraction[1]

    if denominator == 0:
        raise ZeroDivisionError()

    if nominator == denominator:
        return (1, 1)

    if is_prime(nominator) and is_prime(denominator):
        return fraction

    if is_prime(max(nominator, denominator)):
        return fraction

    if denominator % nominator == 0:
        return (1, denominator / nominator)

    if nominator % denominator == 0:
        return (nominator / denominator, 1)

    potential_prime_divisors = generate_primes(min(nominator, denominator))
    for divisor in potential_prime_divisors:
        if nominator % divisor == 0 and denominator % divisor == 0:
            nominator /= divisor
            denominator /= divisor
    return (nominator, denominator)

def collect_fractions(fractions):
    if not isinstance(fractions, list):
        raise Exception('You should enter a list of two tuples!')
    if not len(fractions) == 2:
        raise Exception('You should enter a list of two tuples!')
    if not isinstance(fractions[0], tuple) or not isinstance(fractions[1], tuple):
        raise Exception('You should enter a list of two tuples!')

    first_nominator = fractions[0][0]
    first_denominator = fractions[0][1]
    second_nominator = fractions[1][0]
    second_denominator = fractions[1][1]

    if first_denominator == 0 or second_denominator == 0:
        raise ZeroDivisionError()

    if first_denominator == second_denominator:
        return (first_nominator + second_nominator, first_denominator)

    sum_nominators = first_nominator * second_denominator + second_nominator * first_denominator
    sum_of_fractions = (sum_nominators, first_denominator * second_denominator)
    return simplify_fraction(sum_of_fractions)

def ratio(fraction):
    return fraction[0] / fraction[1]

def sort_fractions(fractions):
    if not isinstance(fractions, list):
        raise Exception('You should enter a list of tuples!')
    for fraction in fractions:
        if not isinstance(fraction, tuple):
            raise Exception('You should enter a list of two tuples!')
    for fraction in fractions:
        if fraction[1] == 0:
            raise ZeroDivisionError
    return sorted(fractions, key = ratio)

if __name__ == '__main__':
    main()
