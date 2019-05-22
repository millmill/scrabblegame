class Tile:

    def __init__(self, letter="E", value=1):
        self.letter = letter
        self.value = value

        # Tile class will hold numerical value of the tile
        # and it's actual corresponding letter.

    def get_value(self):
        # It will return numerical value of tile when requested.
        return self.value

    def get_letter(self):
        # It will return letter of tile when requested.
        return self.letter

    def __str__(self):
        output = self.letter
        if len(str(self.value)) == 1:
            output += " "
        output += str(self.value)
        return output


def main():
    t = Tile()
    print(t)


if __name__ == "__main__":
    main()
