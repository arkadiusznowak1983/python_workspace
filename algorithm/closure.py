# closure example
def outer(attribute):
    attribute = attribute

    def inner():
        return attribute
    return inner


def another_function(param):
    print(param())


if __name__ == "__main__":
    closure = outer('Test value')
    another_function(closure)
