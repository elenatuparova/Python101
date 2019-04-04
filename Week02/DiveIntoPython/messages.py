def numbers_to_message(pressed_sequence):
    keyboard = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    message = ''
    current_button = str(pressed_sequence[0])
    repeated = 1
    is_upper = (current_button == '1')
    for key in pressed_sequence[1:]:
        if str(key) == current_button:
            repeated += 1
        else:
            if str(key) == '0':
                if current_button not in [' ', '0', '1', '-1']:
                    character = keyboard[current_button][(repeated - 1) % len(keyboard[current_button])]
                    message += character.upper() if is_upper else character
                message += ' '
                current_button = ' '
                repeated = 0
                is_upper = False
            elif str(key) == '1':
                if current_button not in [' ', '0', '1', '-1']:
                    character = keyboard[current_button][(repeated - 1) % len(keyboard[current_button])]
                    message += character.upper() if is_upper else character
                current_button = ' '
                repeated = 0
                is_upper = True
            elif str(key) == '-1':
                if current_button not in [' ', '0', '1', '-1']:
                    character = keyboard[current_button][(repeated - 1) % len(keyboard[current_button])]
                    message += character.upper() if is_upper else character
                repeated = 0
                is_upper = False
            else:
                if current_button not in [' ', '0', '1', '-1']:
                    character = keyboard[current_button][(repeated - 1) % len(keyboard[current_button])]
                    message += character.upper() if is_upper else character
                    is_upper = (current_button == '1')
                current_button = str(key)
                repeated = 1

    if current_button not in [' ', '0', '1', '-1']:
        character = keyboard[current_button][(repeated - 1) % len(keyboard[current_button])]
        message += character.upper() if is_upper else character

    return message


def message_to_numbers(message):
    letters = {'a': '2', 'b': '22', 'c': '222', 'd': '3', 'e': '33', 'f': '333',
'g': '4', 'h': '44', 'i': '444', 'j': '5', 'k': '55', 'l': '555', 'm': '6', 'n': '66', 'o': '666',
'p': '7', 'q': '77', 'r': '777', 's': '7777', 't': '8', 'u': '88', 'v': '888',
'w': '9', 'x': '99', 'y': '999', 'z': '9999'}
    key_sequence = []
    for character in message:
        print(character)
        if character.isupper():
            key_sequence.append('1')

        key_sequence.append(letters[character])
    return key_sequence