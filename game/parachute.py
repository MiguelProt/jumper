from os import remove
from game.terminal_service import TerminalService

class Parachute:
    """The Class will draw the parachute
    
    The responsibility of Parachute is to draw the parachute and
    remove lines of the parachute when is neccesary
    
    Attributes:
        __opportunities(list) = will content the parachute and will be used to know how many atemps the user have.
        __body(list) = this will content the body
    """

    def __init__(self):
        self.__opportunities = [
            " _____",
            "/_____\\",
            "\\     /",
            " \\   /",
            "   O"
        ]
        self.__body = [
            "  /|\\",
            "  / \\",
            "",
            "^^^^^^^^^",
        ]
        self.__terminal = TerminalService()

    def print_complete_parachute(self):
        """
        This will print the entire parachute
        """
        for line in self.__opportunities:
            self.__terminal.write_text(line)
        for line in self.__body:
            self.__terminal.write_text(line)

    def get_opportunities(self):
        return len(self.__opportunities) - 1

    def remove_an_opportunity(self, index):
        "This method will remove one line from the parachute (__opportunities)"
        self.__opportunities.pop(index)
        if len(self.__opportunities) == 1:
            self.__opportunities[0] = "   x"