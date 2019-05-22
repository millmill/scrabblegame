from Tile import Tile


class Square:
    def __init__(self, colour="default", tile_multiplier=1, word_multiplier=1, has_tile=None,
                 position=[0, 0]):
        self.colour = colour
        self.tile_multiplier = tile_multiplier
        self.word_multiplier = word_multiplier
        self.has_tile = has_tile
        self.position = position

        #   Each individual square will be one of possible color types,
        #   has tile multiplier of at least 1, some x2 or x3,
        #   has word multiplier of at least 1, some x2 or x3.
        #   It will contain tile placed onto them
        #   position x, y coordinates.

    def get_colour(self):
        #   will return colour of square for GUI to display
        return self.colour

    def get_position(self):
        #   it will return x, y coordinates (position) of square in matrix
        return self.position

    def is_occupied(self):
        #   check if any of the tile is already placed on this square
        return self.has_tile is not None

    def get_tile(self):
        #   if square is occupied by tile, it will return tile object where we
        #   can access it's attributes
        if self.is_occupied():
            return self.has_tile

    def remove_tile(self, tile):
        self.has_tile = None

    def place_tile(self, tile):
        self.has_tile = tile

    def get_letter_score(self):
        #   Will return total score for the square, ie.
        #   value of the tile placed multiplied by x1, x2 or x3.
        if self.is_occupied():
            return self.has_tile.get_value() * self.word_multiplier

    def get_word_multiplier(self):
        #   Return word multiplier x1, x2, x3, which will be used to
        #   multiply total score for the word.
        return self.word_multiplier

    def __str__(self):
        tile = "None"
        line = "---------------"
        if self.is_occupied():
            tile = self.get_tile().__str__()  # string/print version of Tile object

        return (line + "\n" +
                "colour: " + self.colour + "\n" +
                "t.mult: " + str(self.tile_multiplier) + "\n" +
                "w.mult: " + str(self.word_multiplier) + "\n" +
                "Tile: " + tile + "\n" +
                "Position: " + str(self.position[0]) + " " + str(self.position[1]) + "\n" +
                line)


def main():
    t = Tile()
    sq = Square()
    print(sq)
    sq.place_tile(t)
    print(sq)


if __name__ == "__main__":
    main()
