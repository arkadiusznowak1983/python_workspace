def immutable_integer_reference():
    '''
    consequences of immutable integer when using a reference

    Result:
    caller test1 140731340559120 100
    function_with_no_return 140731340559120 100
    function_with_no_return 2342833198928 10000         <- new reference and new value
    caller test1 140731340559120 100                    <- caller still using old reference with old value

    caller test2 2342840162480 1000
    function_with_return 2342840162480 1000
    caller test2 2342833198928 1000000                  <- caller lost old param reference and uses new one
                                                           returned from function, new value visible

    Conclusion:
    Use ctypes if you need that reference back.
    Or pass variable as array element (like: [param]), lists are mutable
    '''
    def caller():
        # test1 only passing by reference
        param = 100
        print('caller test1', id(param), param)
        function_with_no_return(param)
        print('caller test1', id(param), param, '\n')

        # test2 passing and returning by reference
        param = 1000
        print('caller test2', id(param), param)
        # below we assigning new reference to param, new value also of course
        param = function_with_return(param)
        print('caller test2', id(param), param)

    def function_with_no_return(param):
        print('function_with_no_return', id(param), param)
        # below operation *= will implicitly do:
        # new_var = param * param       <- create new variable
        # param = new_var               <- assign new variable reference (not value) to param (param points to new_var)
        param *= param
        print('function_with_no_return', id(param), param)

    def function_with_return(param):
        print('function_with_return', id(param), param)
        # if param*param != param (means value changed) then new variable is created and its reference is returned
        return param*param

    if __name__ == "__main__":
        caller()


# immutable_integer_reference()


##################################################
# below file operations read/write/copy text and bin
##################################################
import sys
from os import strerror
from datetime import datetime
file = 'file_to_read_and_write.txt'
file_bin = 'file_to_read_and_write.docx'

def copy_file_inline_bytearray():
    try:
        with open(file_bin, "rb") as f:
            data = bytearray(f.read())
            f.close()
        with open('copy'+file_bin, "wb") as f:
            f.write(data)
            f.close()
    except IOError as e:
        sys.stderr.write(strerror(e.errno))
    except Exception as e:
        sys.stderr.write(str(e))


def for_loop_through_opened_file():
    try:
        for line in open(file, "r", encoding="UTF-8"):
            print(line)
    except IOError as e:
        sys.stderr.write(strerror(e.errno))
    except Exception as e:
        sys.stderr.write(str(e))


def copy_bin_file():
    buffer = bytearray(65536)
    try:
        with open(file_bin, "rb") as f:
            size = f.readinto(buffer)
            f.close()
        with open('copy'+file_bin, "wb") as f:
            f.write(buffer[:size])
            f.close()
    except IOError as e:
        sys.stderr.write(strerror(e.errno))
    except Exception as e:
        sys.stderr.write(str(e))


def read_and_append_text_file():
    new_text = [f'\n\n{datetime.now().strftime("%H:%M:%S")} New run\n']
    try:
        with open(file, "r+", encoding="UTF-8") as f:
            new_text += f.readlines()
            f.writelines(new_text)
            f.close()
    except IOError as e:
        sys.stderr.write(strerror(e.errno))
    except Exception as e:
        sys.stderr.write(str(e))


##################################################
# below SANDBOX
##################################################
"""
# x = list("abcdEfghi")
# y = list(map(lambda x: chr(ord(x)+(32 if x.isupper() else -32)), x))
# print(y)


# x = list("abcdEfghi")
# y = list(filter(lambda x: x.islower(), x))
# print(y)

#
# def store():
#     inner_store = []
#
#     def add(new):
#         inner_store.append(new)
#
#     def get(index=None):
#         return inner_store[index] if index is not None else inner_store
#     return add, get
#
# add, get = store()
# add(2)
# print(get(0))
# add(3)
# add(4)
# print(get(2))
# print(get())

# def print_decorator(func, debug=True):
#     buffer = []
#     def get(index=None):
#         if index is not None and index < len(buffer):
#             return buffer[index]
#         else:
#             return buffer
#
#     def add(*args):
#         line = args[0]
#         buffer.append(line)
#         if debug:
#             func(line)
#     return add, get
#
# print, get = print_decorator(print, False)
# print('test message')
# print('second message')
# print('third message')
# print(get(1))
#
#

# x = [2, 5, 3, 1]
# def bit_or(x): return x | 1
# y = map(bit_or, x)
# print([i for i in x])
"""
