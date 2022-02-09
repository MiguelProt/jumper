class Jumper:

    def __init__(self):
        self.__guess_history = []

    def validate_letter(self, letter):
        """
        Check this function and the logic to prevent use the same letter twice
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