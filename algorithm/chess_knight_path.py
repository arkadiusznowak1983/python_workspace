class Position:
    x: int
    y: int

    def __init__(self, x: int, y: int):
         self.x = x
         self.y = y

    def show(self):
        return f"{self.x}, {self.y}"


class Knight:
    position: Position
    table = {}
    path = []
    complexity = 0

    def __init__(self, position: Position, path=[]):
        self.position = position
        self.path = path
        Knight.complexity = Knight.complexity + 1

        if self.position.show() not in Knight.table:
            Knight.table[self.position.show()] = self.path
        else:
            current_path = Knight.table[self.position.show()]
            if len(current_path) > len(self.path):
                Knight.table[self.position.show()] = self.path
                for pos, field in Knight.table.items():
                    if str(field)[:-1].startswith(str(current_path+[self.position.show()])[:-1]):
                        Knight.table[pos] = self.path + field[len(current_path):]
            return

        for move_type in range(1, 9):
            self.move(move_type)

    def move(self, move_type):
        if move_type == 1:
            x, y = 1, 2
        if move_type == 2:
            x, y = 2, 1
        if move_type == 3:
            x, y = 2, -1
        if move_type == 4:
            x, y = 1, -2
        if move_type == 5:
            x, y = -1, -2
        if move_type == 6:
            x, y = -2, -1
        if move_type == 7:
            x, y = -2, 1
        if move_type == 8:
            x, y = -1, 2
        new_x = self.position.x + x
        new_y = self.position.y + y
        if not self.check(new_x, new_y):
            return
        Knight(Position(new_x, new_y), self.path + [self.position.show()])

    def check(self, x, y):
        if x < 1 or x > 8:
            return False
        if y < 1 or y > 8:
            return False
        if len(self.path) and x == self.path[-1]:
            return False
        return True

    @staticmethod
    def get_shortest_path(position: Position):
        return Knight.table.get(position.show(), False)


if __name__ == '__main__':
    column_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    Knight(Position(column_map['B'], 1))
    print(f"Shortest path from B1 to E8 is {Knight.get_shortest_path(Position(column_map['E'], 8))}")
    print(f"Total number of possible paths is {Knight.complexity}")