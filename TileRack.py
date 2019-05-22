from Tile import Tile
from TileBag import TileBag
from Square import Square


class TileRack(Square):

    def __init__(self, rack_size=7):  # array of Tile objects
        self.rack_size = rack_size
        self.rack_array = [Square() for i in range(self.rack_size)]

        for col in range(self.rack_size):
            sq = self.rack_array[col]
            sq.position = [0, col]
        #   Size of tile rack will be always 7 while there are
        #   tiles remaining in TileBag.
        #   Tiles will be stored in array and we can access them by their index.

    def __iter__(self):
        for square in self.rack_array:
            yield square

    def __getitem__(self, i):
        #   support for indexing
        return self.rack_array[i]

    def is_full(self):
        #   Check if the rack has all 7 tiles in it.
        #   not if it has 7 square objects, always has
        for sq in self.rack_array:
            if sq.get_tile() is None:
                return False
        return True        

    def is_empty(self):
        #   Check if the rack is empty, if there are no tiles in the rack.
        #   not if it has 7 square objects, always has
        for sq in self.rack_array:
            if sq.get_tile() is not None:
                return False
        return True

    def take_tile(self, i):  
        #   index of Tile in rackArray
        #   When player play their tile onto the board, it will be
        #   removed from an array of tiles and
        #   the size of the rack will be reduced by 1.
        return self.rack_array[i].get_tile()

    def replace_tile(self, tile):
        pass

    def refill_rack(self, tile_bag):
        #   MAKE SURE TO PASS INSTANCE OF THE BAG to take tiles from!!!
        for sq in self.rack_array:
            if not sq.is_occupied():
                sq.place_tile(tile_bag.take_tile())

    def __str__(self):
        s = ""
        for sq in self.rack_array:
            if sq.is_occupied():
                s += ("|" + sq.get_tile().__str__())
            else:
                s += "|   "
        return s + "|"

def main():
    tile_bag = TileBag()
    tile_rack = TileRack()
    print("tiles in the bag: ", len(tile_bag))
    print(tile_rack) 
    print("tile rack is empty", tile_rack.is_empty())
    print()  
    tile_rack.refill_rack(tile_bag)
    print("tiles in the bag after refilling rack: ", len(tile_bag))
    print(tile_rack)
    print("tile rack is full:", tile_rack.is_full())

if __name__ == "__main__":
    main()
