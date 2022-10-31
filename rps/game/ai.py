import random
from game.player import Player

class Ai(Player):
    """The artificial intelligent that the player plays against. 
    
    The responsibility of the Ai is to choose between rock, paper or scissor to beat the player.
    
    Attributes:
        actual_form (string): the current form of the Ai's hand represented in numbers, 1: rock, 2: paper, 3: scissors.
        score (int): The amount of wins the Ai has.
        forms_list (list): A list with the possible forms represented by numbers (1,2 and 3)
    """
    def __init__(self):
        """Constructs a new Ai.

        Args:
            self (Ai): An instance of Ai.
        """
        super().__init__()
        self._forms_list = ["1","2","3"]       


    def set_form(self,choice):
        """Set the actual form randomly.

        Args:
            self (Player): An instance of Ai.
            choice (string): a string number, could be 1, 2 or 3, (since this is an overriden method, this argument is not needed in this class).
        """
        self._actual_form = random.choice(self._forms_list)

