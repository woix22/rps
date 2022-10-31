from game.player import Player
from game.ai import Ai
from game.logic import Logic
from game.terminal_service import Terminal_service

class Director():
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        player (Player): The game's player.
        ai (Ai): The game's Ai.
        players (list): A list with both player and ai
        logic (Logic): the game's logic
        ts (Terminal_service): For getting and displaying information on the terminal
        wins (int): The amount of wins to win the game
        is_playing (boolean): Whether or not to keep playing.
        final_result: the final result of the game
        messages (dictionary): messages used during the game.
    """
    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.player = Player()
        self.ai = Ai()
        self.players = [self.player, self.ai]
        self.logic = Logic()
        self.ts = Terminal_service()
        self._wins = 0
        self._is_playing = True
        self._final_result = ""
        self._messages = {"choice":"""
1) ROCK
2) PAPER
3) SCISSORS

MAKE YOUR CHOICE: """,
                        "wins":""""
1) 3 WINS
2) 5 WINS
3) 10 WINS

HOW MANY WINS DO YOU WANT TO PLAY?: """,
                        "again":"""
DO YOU WANT TO PLAY AGAIN? (Y/N) """}

    def set_wins(self,option):
        """Set the amount of wins.

        Args:
            option (string): The option represented by a number.            
        """
        options = {"1":3,
        "2":5,
        "3":10}
        self._wins = options[option]

    def get_wins(self):
        """Gets the amount of wins.
        
        Returns:
            int: The amount of wins.
        """
        return self._wins

    def set_final_result(self,result):
        """Set the final result.

        Args:
            result (string): The final result represented by a letter.            
        """
        self._final_result = result

    def get_final_result(self):
        """Gets the final result.
        
        Returns:
            string: The final result represented by a letter.
        """
        return self._final_result

    def get_message(self,message):
        """Gets a message from a list.
        
        Returns:
            string: A message.
        """
        return self._messages[message]   


    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._game_loop()

    def _game_loop(self):
        """The game loop, this will continue looping until the player decides to not to play anymore.

        Args:
            self (Director): an instance of Director.
        """
        wins = self.ts.get_input(self.get_message("wins"),["1","2","3"])
        self.set_wins(wins)
        while self.player.get_score() < self.get_wins() and self.ai.get_score() < self.get_wins():
            choice = self.ts.get_input(self.get_message("choice"),["1","2","3"])
            for player in self.players:                
                player.set_form(choice)
            player_form = self.player.get_form()
            ai_form = self.ai.get_form()
            combination = self.logic.get_combination(player_form,ai_form)
            result = self.logic.compare_hands(combination)
            self.ts.print_hands(combination)
            self.ts.print_result(result)
            if result == "w":
                self.player.add_point()
            elif result == "l":
                self.ai.add_point()
            player_score = self.player.get_score()
            ai_score = self.ai.get_score()
            wins_string = str(self.get_wins())
            self.ts.print_current_score(player_score,ai_score,wins_string)
        if self.player.get_score() > self.ai.get_score():
            self.set_final_result("w")
        elif self.player.get_score() < self.ai.get_score():
            self.set_final_result("l")
        self.ts.print_final_result(self.get_final_result())
        again = self.ts.get_input(self.get_message("again"),["Y","y","N","n"])
        if again == "n" or again == "N":
            self._is_playing = False
        for player in self.players:                
            player.reset_score()