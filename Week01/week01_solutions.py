import math

#task 2
def to_digits(n):
    n = abs(n)
    return [int(ch) for ch in str(n)]

#task 1
def sum_of_digits(n):
    digits = to_digits(n)
    return sum(digits)

#task 3
def join(items, delimiter):
    result = ''
    for index in range(len(items)):
        result += str(items[index])
        if index != len(items) - 1:
            result += delimiter
    return result

def to_number(digits):
    return int(join(digits, ''))

#task 4
def fact(n):
    if n in [0, 1]:
        return 1
    result = 1
    for x in range(n):
        result *= x + 1
    return result

def fact_digits(n):
    return sum([fact(digit) for digit in to_digits(n)])

#task 5
def palindrome(obj):
    is_palindrome = True
    string_obj = str(obj)
    n = len(string_obj) - 1
    i = 0
    j = n
    while i <= n // 2:
        if string_obj[i] != string_obj[j]:
            is_palindrome = False
            break
        i += 1
        j -= 1
    return is_palindrome

#tasks 6 and 7
def count_letters(str, letters):
    number_letters = 0
    str = str.lower()
    for ch in str:
        if ch in letters:
            number_letters += 1
    return number_letters

#task 6
def count_vowels(str):
    vowels = 'aeiouy'
    return count_letters(str, vowels)

#task 7
def count_consonants(str):
    consonants = 'bcdfghjklmnpqrstvwxz'
    return count_letters(str, consonants)

#task 8
def char_histogram(string):
    char_occurences = {}
    for char in string:
        if char not in char_occurences:
            char_occurences[char] = 0
        char_occurences[char] += 1
    return char_occurences

#task 9
def sum_matrix(m):
    result = 0
    for i in range(len(m)):
        result += sum(m[i])
    return result

#task 10
def nan_expand(times):
    expansion = '"'
    while times > 0:
        expansion += 'Not a '
        if times == 1:
            expansion += 'NAN'
        times -= 1
    expansion += '"'
    print(expansion)

#task 11
def generate_primes(upperbound):
    primes = []
    is_prime = True
    for num in range(2, upperbound + 1):
        is_prime = True
        for divisor in range (2, int(math.sqrt(upperbound))):
            if num % divisor == 0 and divisor != num:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def prime_factorization(n):
    prime_factorization = []
    primes = generate_primes(n)
    current_state = n
    current_power = 0
    for prime in primes:
        while (current_state % prime == 0):
            current_power += 1
            current_state //= prime
        if current_power:
            prime_factorization.append((prime, current_power))
        current_power = 0
    return prime_factorization

#task 12
def group(items):
    groups = [[items[0]]]
    current_group = 0
    for i in range(1, len(items)):
        if items[i] == items[i - 1]:
            groups[current_group].append(items[i])
        else:
            current_group += 1
            groups.append([items[i]])
    return groups

def max_consecutive(items):
    consecutive_groups = group(items)
    sizes = [len(x) for x in consecutive_groups]
    return max(sizes)