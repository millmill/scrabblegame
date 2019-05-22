from Tile import Tile
from random import randint, shuffle


class TileBag(Tile):

    def __init__(self, bag_size=100):
        super().__init__()
        self.bag_size = bag_size
        self.bag_array = []
        #   Tile Bag will contains all starting tiles for the game and
        #           
        #   they will be stored in an array#
        #   Player will be able to remove tiles and to add them to his rack. 

        for letter, val in letter_dict.items():
            score, amount = val
            for i in range(amount):
                self.bag_array.append(Tile(letter, score))
        shuffle(self.bag_array)

    def replace_tiles(self, swapped_tiles):
        for tile in swapped_tiles:
            print(tile)
            self.bag_array.append(Tile(tile[0], tile[1]))
        shuffle(self.bag_array)

    def take_tile(self):
        #   If the bag is not empty,
        #   remove tile from the bag and decrement size of the bag.
        if not self.is_empty():
            return self.bag_array.pop()

    def __getitem__(self, i):
        return self.bag_array[i]

    def __iter__(self):
        for tile in self.bag_array:
            yield tile

    def __len__(self):
        return len(self.bag_array)
        
    def is_empty(self):
        #  Will check if bag size is equal 0, ie. the bag is empty.
        return len(self.bag_array) == 0

    def __str__(self):
        s = ""
        for tile in self.bag_array:
            s += ("[" + tile.__str__() + "]")
        return s


letter_dict = {
        "A": [1, 9],
        "B": [3, 2],
        "C": [3, 2],
        "D": [2, 4],
        "E": [1, 12],
        "F": [4, 2],
        "G": [2, 3],
        "H": [4, 2],
        "I": [1, 9],
        "J": [8, 1],
        "K": [5, 1],
        "L": [1, 4],
        "M": [3, 2],
        "N": [1, 6],
        "O": [1, 8],
        "P": [3, 2],
        "Q": [10, 1],
        "R": [1, 6],
        "S": [1, 4],
        "T": [1, 6],
        "U": [1, 4],
        "V": [4, 2],
        "W": [4, 4],
        "X": [8, 1],
        "Y": [4, 2],
        "Z": [10, 1],
        }
        # "#": [0, 2],
        # }


def main():
    tb = TileBag()
    print(tb)
    print(tb.take_tile())
    print(tb)


if __name__ == "__main__":
    main()
