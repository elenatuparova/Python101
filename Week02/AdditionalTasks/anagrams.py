def anagrams():
    first_string = input()
    second_string = input()
    result = 'ANAGRAMS' if sorted(first_string) == sorted(second_string) else 'NOT ANAGRAMS'
    return result