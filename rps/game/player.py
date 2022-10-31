class Player():
    """The user playing this game. 
    
    The responsibility of the player is to choose between rock, paper or scissor to beat the AI.
    
    Attributes:
        actual_form (string): the current form of the player's hand represented in numbers, 1: rock, 2: paper, 3: scissors.
        score (int): The amount of wins the player has.
    """
    def __init__(self):
        """Constructs a new Player.

        Args:
            self (Player): An instance of Player.
        """
        self._actual_form = ""
        self._score = 0

    def set_form(self,choice):
        """Set the actual form.

        Args:
            self (Player): An instance of Player.
            choice (string): a string number, could be 1, 2 or 3
        """
        self._actual_form = choice

    def get_form(self):
        """Gets the actual form.
        
        Returns:
            string: The actual form.
        """
        return self._actual_form

    def add_point(self):
        """Adds 1 point to the player's score.

        """
        self._score += 1

    def get_score(self):
        """Gets the current score from the player.
        
        Returns:
            int: The current score.
        """
        return self._score

    def reset_score(self):
        """Resets the score to 0.

        """
        self._score = 0
