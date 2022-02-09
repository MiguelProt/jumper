class Jumper:
    """The jumper class will manage the guessed letters from the user
    
    The responsibility of this class is to save the letter that the user is guessing
    and validate if the letter was guessed before
    
    Attributes:
        __guess_history (list): The list of the letters that the user guessed
    """
    def __init__(self):
        self.__guess_history = []

    def validate_letter(self, letter):
        """
        This method check if word exist and the logic to prevent use the same letter twice
        """
        valide_letter = True
        print(self.__guess_history)
        if len(self.__guess_history) == 0:
            self.save_history(letter)
            valide_letter = True
            print(self.__guess_history)
        else:
            for single_letter in self.__guess_history:
                if single_letter == letter:
                    return False
                self.save_history(letter)
        print(valide_letter)
        return valide_letter

    def save_history(self, letter):
        self.__guess_history.append(letter)
    
    def get_history(self):
        return self.__guess_history