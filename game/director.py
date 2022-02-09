from game.terminal_service import TerminalService
from game.hider import Hider
from game.jumper import Jumper
from game.parachute import Parachute


class Director:

    def __init__(self):
        self.__hider = Hider()
        self.__is_playing = True
        self.__jumper = Jumper()
        self.__terminal_service = TerminalService()
        self.__parachute = Parachute()
        
    def start_game(self):
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
        status = self.__hider.get_status()
        for letter in status:
            print(f"{letter} ", end="")
        print("\n")
        self.__parachute.print_complete_parachute()
    
    def _get_inputs(self):
        new_guessing = self.__terminal_service.read_text("\nGuess a letter [a-z]: ")
        self.__jumper.save_history(new_guessing)
        return new_guessing

    def __do_updates(self, guessed_letter):
        letter_found = self.__hider.update_guessed_word(guessed_letter)
        if not letter_found and guessed_letter != '':
            self.__parachute.remove_an_opportunity(0)

    def __keep_play(self):
        keep_playing = True
        opportunities = self.__parachute.get_opportunities()
        word_found = self.__hider.word_found()

        if word_found == True:
            print("Winner!")
            keep_playing = False
        elif opportunities <= 0: 
            print("You Fail!")
            keep_playing = False
        return keep_playing