def int_decorator(function):
    no_value = '0'

    def wrapper(*args):
        try:
            return function(*args)
        except:
            return function(no_value)
    return wrapper


int = int_decorator(int)

assert int(1.23) == 1
assert int('1.12') == 0
assert int('12') == 12
assert int('a') == 0
assert int('a1') == 0

print(int(1.23), int('1.12'), int('12'), int('a'), int('a1'))
