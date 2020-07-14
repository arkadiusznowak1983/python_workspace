class RecursiveToLinear:
    def sample_recursive(self, nestedArray=[]):
        for value in nestedArray:
            if isinstance( value, list ):
                self.sample_recursive( value )
            else:
                print( value )
        return True

    def sample_linear(self, nestedArray=[]):
        arrays = []
        arraysLeft = nestedArray.copy()

        while(len(arraysLeft)):
            arrays = arraysLeft.copy()
            arraysLeft = []
            for value in arrays:
                if isinstance(value, list):
                    arraysLeft = value
                    break
                print( value )

        # [1, 2, [9, 8, [1, 1]], [1, 1, 2, 5], 3]

        print( arrays )
        return True