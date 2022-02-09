import random

class Hider:
    """The person hiding from the Seeker. 
    
    The responsibility of Hider is to keep track of its location and distance from the seeker. 
    
    Attributes:
        _words (list): The list of available words
        _word_to_find: the random word to find
    """
    def __init__(self):
        #self.__words = ["hulk", "chronos", "ship", "animal"]
        self.__words = ["animal"]
        self.__word_to_find = list(random.choice(self.__words))
        self.__guessed_word = self.__init_guessed_word()
        self.__init_guessed_word()

    def __init_guessed_word(self):
        index = 0
        temp_guessed_word = []
        for letter in self.__word_to_find:
            temp_guessed_word.insert(index, "_")
            index += 1
        return temp_guessed_word

    def get_status(self):
        return self.__guessed_word

    def update_guessed_word(self, player_letter):
        index = 0
        letter_found = False
        for letter in self.__word_to_find:
            if letter == player_letter.lower():
                self.__guessed_word[index] = letter
                letter_found = True
            index += 1
        return letter_found

    def word_found(self):
        for letter in self.__guessed_word:
            if letter == "_":
                return False
        return True


"""
h = Hider()
print(h.show_status()["opportunities"])
print(h.update_status())
print()
for line in h.get_opportunities():
    print(line)
"""