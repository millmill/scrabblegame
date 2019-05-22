from Square import Square
from Tile import Tile
from random import randint


class Board(Square):

    def __init__(self, size=15):
        super().__init__()
        self._size = size
        self._square_array = [[Square() for i in range(self._size)] for j in range(self._size)]

        for row in range(self._size):
            for col in range(self._size):
                sq = self._square_array[row][col]
                sq.position = [row, col]

        #   Size of the board correspond to how many rows and columns it will have.
        #   All the squares will be held in an arrays, which will create a matrix.

    def __iter__(self):
        for row in self._square_array:
            for square in row:
                yield square

    def __getitem__(self, coords):
        #   support for indexing
        #   usage: single int for iterative position or tuple
        #   board[80], board[5][13]
        x, y = self.parse_coords(coords)
        return self._square_array[x][y]

    def parse_coords(self, coords):
        if isinstance(coords, int):
            x = coords // self._size
            y = coords % self._size
        else:
            x = coords[0]
            y = coords[1]

        if x < self._size and y < self._size:
            return x, y

    def get_square(self, coords):
        #   usage: single int for iterative position or tuple for x, y
        #   board[80], board[5][13]
        x, y = self.parse_coords(coords)
        return self._square_array[x][y]

    def place_tile(self, coords, tile):
        #   coords must be tuple or an array of length 2
        #   Based on square's x, y coordinates, it will place
        #   tile into correct position on the board.
        x, y = self.parse_coords(coords)
        self._square_array[x][y].place_tile(tile)

    def make_board(self):
        #   use with newly created instance of board only (blank boards)
        doubleL = Tile("doubleL", 0)
        tripleL = Tile("tripleL", 0)
        doubleW = Tile("doubleW", 0)
        tripleW = Tile("tripleW", 0)

        bonus_square_colours = ["doubleL", "tripleL", "doubleW", "tripleW"]
        bonus_square_values = [2, 3, 2, 3]

        #   creating random amount of bonus squares
        double_letter = randint(15, 25)  # 20
        triple_letter = randint(9, 15)   # 12
        double_word =   randint(12, 20)  # 16
        triple_word =    randint(6, 10)  # 8

        for idx, num_of_bonus_squares in enumerate([double_letter, triple_letter, double_word, triple_word]):
            while num_of_bonus_squares:
                random_square = self._square_array[randint(0, self._size - 1)][randint(0, self._size - 1)]

                #   changing colour and multipliers for square
                if random_square.colour == "default":
                    multiplier = idx % 2
                    if idx // 2:
                        random_square.word_multiplier = bonus_square_values[multiplier]
                        if idx % 2 == 0:
                            random_square.has_tile = doubleW
                        else:
                            random_square.has_tile = tripleW
                    else:
                        random_square.tile_multiplier = bonus_square_values[multiplier]
                        if idx % 2 == 0:
                            random_square.has_tile = doubleL
                        else:
                            random_square.has_tile = tripleL

                    random_square.colour = bonus_square_colours[idx]
                    num_of_bonus_squares -= 1

    def __str__(self):
        output = ""
        line = ("----" * self._size + "-\n")
        for arr in self._square_array:
            output += line
            for sq in arr:
                if sq.is_occupied():
                    output += ("|" + sq.get_tile().__str__())
                else:
                    if sq.colour != "default":
                        bonus = ""
                        if sq.tile_multiplier == 2:
                            bonus = "dl "
                        elif sq.tile_multiplier == 3:
                            bonus = "tl "
                        elif sq.word_multiplier == 2:
                            bonus = "dw "
                        elif sq.word_multiplier == 3:
                            bonus = "tw "
                        output += ("|" + bonus)
                    else:
                        output += "|   "
            output += "|\n"
        output += line
        return output


def main():
    t1 = Tile("R", 1)
    t2 = Tile("X", 8)
    t3 = Tile("Q", 10)
    print("blank board, no tiles")
    b = Board()
    print(b)

    b.place_tile((10, 10), t1)
    b.place_tile([5, 5], t2)
    b.place_tile([6, 6], t3)
    print("board with few tiles placed")
    print(b)

    print("details of individual squares")
    print(b.get_square([3, 3]))
    print(b.get_square([10, 10]))

    print("#############################")
    print("creating random board state for new game")
    b2 = Board()
    b2.make_board()
    print("printing first 20 squares")
    for i in range(20):
        print(b2[i])
    b2.place_tile((13, 14), t3)
    print(b2)


if __name__ == "__main__":
    main()
