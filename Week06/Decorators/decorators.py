import time

def accepts(*allowed_type):
    def accepter(func):
        def decorated(*args, **kwargs):
            for index, argument in enumerate(args):
                if not isinstance(argument, allowed_type[index]):
                    raise TypeError('Argument {} of {} is not {}'.format(index + 1, func.__name__, allowed_type[index]))
            return func(*args, **kwargs)
        return decorated
    return accepter

@accepts(str)
def say_hello(name):
    return("Hello, I am {}".format(name))

@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True


def encrypt(key):
    def accepter(func):
        def decorated(*args, **kwargs):
            message = func(*args, **kwargs)
            encrypted_message = ''
            for char in message:
                if ord(char) in range(65, 91):
                    if ord(char) + key <= 90:
                        encrypted_message += chr(ord(char) + key)
                    else:
                        encrypted_message += chr(64 + key)
                elif ord(char) in range(97, 123):
                    if ord(char) + key <= 122:
                        encrypted_message += chr(ord(char) + key)
                    else:
                        encrypted_message += chr(96 + key)
                else:
                    encrypted_message += char
            return encrypted_message
        return decorated
    return accepter

@encrypt(2)
def get_low():
    return 'Get get get low'


def log(file_name):
    def accepter(func):
        method_name = func.__name__
        def decorated(*args, **kwargs):
            with open(file_name, 'a+') as log_file:
                str_log = '{} was called at {}\n'.format(method_name, time.asctime())
                log_file.write(str_log)
        return decorated
    return accepter

@log('log.txt')
def get_low():
    return 'Get get get low'


def performance(file_name):
    def accepter(func):
        def decorated(*args, **kwargs):
            with open(file_name, 'a+') as log_file:
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                performance = round(end - start, 2)
                str_log = '{} was called and took {} seconds to complete\n'.format(func.__name__, performance)
                log_file.write(str_log)
        return decorated
    return accepter

@performance('performance.txt')
def get_low():
    return 'Get get get low'