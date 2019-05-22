class Dictionary:
    
    def __init__(self):
        self.dictionary = {}
        with open("./dictionaries/english_words_94k.txt", "rb") as eng_words:
            for word in eng_words:
                try:
                    self.dictionary[word.decode("utf-8").strip()] = True
                except UnicodeDecodeError:
                    pass
                    #   if not UTF-8 characters in source file

        #   Will be build from supplied text file which contains
        #   large number of words.
        #   Can be enquired for specific word and it will return
        #   if its valid word or not.
        
    def check_word(self, word):
        #   It will check existence of the word in the dictionary.
        return word.lower() in self.dictionary


def main():
    dic = Dictionary()
    print("'car' in dictionary: ", dic.checkWord("car"))
    print("'xlfsldjdgjf' in dictionary: ", dic.checkWord("xlfsldjdgjf"))


if __name__ == "__main__":
    main()
