import math
class Egsfloor:
    '''

    '''
    def eggDrop(self, eggs=2, floors=10, operation=min):
        if eggs <= 1:
            return floors

        if floors <= 2:
            return 1

        return 1 + operation( self.eggDrop(eggs-1, math.ceil(floors / 4) - 1), self.eggDrop(eggs, floors - math.ceil(floors / 4)) )


