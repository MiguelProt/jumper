from os import remove
from game.terminal_service import TerminalService

class Parachute:

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
        for line in self.__opportunities:
            self.__terminal.write_text(line)
        for line in self.__body:
            self.__terminal.write_text(line)

    def get_opportunities(self):
        return len(self.__opportunities) - 1

    def remove_an_opportunity(self, index):
        self.__opportunities.pop(index)
        if len(self.__opportunities) == 1:
            self.__opportunities[0] = "   x"