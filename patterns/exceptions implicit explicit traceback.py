from traceback import format_tb


class ExplicitException(Exception):
    def __str__(self):
        return f"Error: {self.args} " \
               f"\nImplicit: {self.__context__} " \
               f"\nExplicit: {self.__cause__} " \
               f"\nTrace: {format_tb(self.__traceback__)}"


try:
    1 / 0
except ZeroDivisionError as e0:
    try:
        try:
            [][0]
        except IndexError as ei:
            raise ExplicitException('my explicit exception') from e0
    except ExplicitException as ex:
        print(ex)