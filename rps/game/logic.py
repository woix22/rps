class Logic():
    """Some logic needed to process the information given by the player and Ai.
    
    Attributes:
        combinations (dictionary): All the 9 possible combinations within the game and their results.
        
    """
    def __init__(self):
        """Constructs a new Logic.

        Args:
            self (Logic): An instance of Logic.
        """
        # 1: Rock, 2: Paper, 3: Scissors
        self._combinations = {"11":"d",
                              "12":"l",
                              "13":"w",
                              "21":"w",
                              "22":"d",
                              "23":"l",
                              "31":"l",
                              "32":"w",
                              "33":"d"}

    def get_combination(self,player,ai):
        """Joins both choices and return that combination.
        
        Returns:
            string: The combination.
        """
        combination = player + ai
        return combination
    
    def compare_hands(self,combination):
        """Compares both hands in the combination and uses the combination list to return the result.
        
        Returns:
            string: The result of the combination.
        """
        return self._combinations[combination]

