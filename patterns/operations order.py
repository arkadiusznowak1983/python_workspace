def left():
    raise Exception('left')


def right():
    raise Exception('right')


def check_condition():
    if left() == right():
        print('ok')


class Variable:
    def __init__(self):
        self._v = None

    @property
    def v(self):
        return self._v

    @v.setter
    def v(self, value):
        self._v = value
        raise Exception('left assign')


def check_assign():
    variable = Variable()
    variable.v = right()
    print('ok')



print('[Operations order]')
try: check_condition()
except Exception as e: print('condition: ', e)

try: check_assign()
except Exception as e: print('assign: ', e)
