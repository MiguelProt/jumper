from game.terminal_service import TerminalService
from game.hider import Hider
from game.jumper import Jumper
from game.parachute import Parachute


class Director:
    """
    A person who directs the game.

    The responsability of a Director is to control the sequence of play.

    Attributes:
    __is_playing (bool) = Will determinate if the game continue or is finished
    __hider(Hider) = the game's hider
    __jumper(Jumper) = the game's jumper
    __terminal_service = the game's Terminal Service
    __parachute = the game's parachute

    """

    def __init__(self):
        self.__is_playing = True
        self.__hider = Hider()
        self.__jumper = Jumper()
        self.__terminal_service = TerminalService()
        self.__parachute = Parachute()
        
    def start_game(self):
        """
        Start the game by running the main game loop.
        Args:
            self(Director): an instance of Director
        """
        guessed_letter = ''
        vueltas =  0
        while self.__is_playing:
            self.__show_status()
            guessed_letter = self._get_inputs()
            self.__do_updates(guessed_letter)
            vueltas += 1
            print()
            self.__is_playing = self.__keep_play()
        self.__show_status()

    def __show_status(self):
        """
        This will show the state of the word and the parachute
        Args:
            self(Director): an instance of Director
        """
        status = self.__hider.get_status()
        for letter in status:
            print(f"{letter} ", end="")
        print("\n")
        self.__parachute.print_complete_parachute()
    
    def _get_inputs(self):
        """
        Ask for a letter
        Args:
            self(Director): an instance of Director
        """
        new_guessing = self.__terminal_service.read_text("\nGuess a letter [a-z]: ")
        self.__jumper.save_history(new_guessing)
        return new_guessing

    def __do_updates(self, guessed_letter):
        """
        This method will check if the letter exits or not and will remove part of the
        parachute if is neccesary
        Args:
            self(Director): an instance of Director
            guessed_letter: this is the letter that the user guessed
        """
        letter_found = self.__hider.update_guessed_word(guessed_letter)
        self.__terminal_service.write_text(f"\nThe letter '{guessed_letter}' is not in the word")
        if not letter_found and guessed_letter != '':

            self.__parachute.remove_an_opportunity(0)

    def __keep_play(self):
        """
        This method will check if the game needs to finished
        Args:
            self(Director): an instance of Director
        """
        keep_playing = True
        opportunities = self.__parachute.get_opportunities()
        word_found = self.__hider.word_found()

        if word_found == True:
            self.__terminal_service.write_text("Winner!")
            keep_playing = False
        elif opportunities <= 0: 
            self.__terminal_service.write_text("You Fail!")
            keep_playing = False
        return keep_playing