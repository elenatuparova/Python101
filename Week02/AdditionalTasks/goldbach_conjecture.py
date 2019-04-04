import math

def generate_primes(upperbound):
    primes = []
    is_prime = True
    for num in range(2, upperbound):
        is_prime = True
        for divisor in range (2, int(math.sqrt(upperbound))):
            if num % divisor == 0 and divisor != num:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def goldbach(n):
    primes = generate_primes(n)
    goldbach_conjecture = []

    for prime in primes:
        difference = n - prime
        if difference in primes and (difference, prime) not in goldbach_conjecture:
            goldbach_conjecture.append((prime, difference))

    return goldbach_conjecture