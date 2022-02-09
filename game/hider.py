import random

class Hider:
    """The person hiding from the person who is trying to discover the word. 
    
    The responsibility of Hider is to say if the guess of the user is right or not
    
    Attributes:
        _words (list): The list of available words
        _word_to_find: the random word to find
        _guessed_word: The word that the user will be discovering
    """
    def __init__(self):
        self.__words = ["hulk", "chronos", "ship", "animal"]
        #self.__words = ["animal"]
        self.__word_to_find = list(random.choice(self.__words))
        self.__guessed_word = self.__init_guessed_word()
        self.__init_guessed_word()

    def __init_guessed_word(self):
        """
        This method will assign the right number of '_' based on the self.__word_to_find
        """
        index = 0
        temp_guessed_word = []
        for letter in self.__word_to_find:
            temp_guessed_word.insert(index, "_")
            index += 1
        return temp_guessed_word

    def get_status(self):
        return self.__guessed_word

    def update_guessed_word(self, player_letter):
        """
        This method is created to determinate if the letter that the user guess is 
        inside the word that we need to find. If the letter is inside the word, then we update 
        the self.__guessed_word adding the letter in the right index and returning a bool value.
        """
        index = 0
        letter_found = False
        for letter in self.__word_to_find:
            if letter == player_letter.lower():
                self.__guessed_word[index] = letter
                letter_found = True
            index += 1
        return letter_found

    def word_found(self):
        """
        We read all the guessed word and if there's an '_' inside the word, then there is 
        a word that we need to discover
        """
        for letter in self.__guessed_word:
            if letter == "_":
                return False
        return True