class Terminal_service():
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """

    def get_input(self,message,condition):
        """Gets and validates the input by the user.

        Args:
            message (string): The text message shown before the input.
            condition (list): a list with all the valid options to answer.

        Returns:
            choice (string): The user's choice 
        """

        while True:
            try:
                choice = input(message)
            except ValueError:
                print("\nInvalid input\n")
                continue
            
            if choice not in condition:
                print("\nInvalid input\n") 
                continue            
            else: break     
        return choice 
        


    def print_hands(self,combination):
        """Prints the hands of the given combination.

        Args:
            combination (string): the combination.            
        """
        hands = {"11": """
    ROCK                   ROCK
    _______      |      _______
---'   ____)     |     (_      '---
      (_____)    |    (_
      (_____)    |    (_
      (____)     |     (
---.__(___)      |      (______.---
                 |
                 """,
                 "12": """
    ROCK                       PAPER
    _______      |           _______
---'   ____)     |      ____(____   '---
      (_____)    |     (______
      (_____)    |    (_______
      (____)     |     (_______
---.__(___)      |       (__________.---
                 |
                 """,
                 "13": """
    ROCK                    SCISSORS
    _______      |           _______
---'   ____)     |      ____(____   '---
      (_____)    |     (______
      (_____)    |    (_______
      (____)     |          (__
---.__(___)      |           (______.---
                 |
                 """,
                 "21": """
    PAPER                       ROCK
    _______           |      _______
---'   ____)____      |     (_      '---
          ______)     |    (_
          _______)    |    (_
         _______)     |     (
---.__________)       |      (______.---
                      |
                 """,
                 "22": """
    PAPER                           PAPER
    _______           |           _______
---'   ____)____      |      ____(____   '---
          ______)     |     (______
          _______)    |    (_______
         _______)     |     (_______
---.__________)       |       (__________.---
                      |
                 """,
                 "23": """
    PAPER                        SCISSORS
    _______           |           _______
---'   ____)____      |      ____(____   '---
          ______)     |     (______
          _______)    |    (_______
         _______)     |          (__
---.__________)       |           (______.---
                      |
                 """,
                 "31": """
    SCISSORS                    ROCK
    _______           |      _______
---'   ____)____      |     (_      '---
          ______)     |    (_
       __________)    |    (_
      (____)          |     (
---.__(___)           |      (______.---
                      |
                 """,
                 "32": """"
    SCISSORS                        PAPER
    _______           |           _______
---'   ____)____      |      ____(____   '---
          ______)     |     (______
       __________)    |    (_______
      (____)          |     (_______
---.__(___)           |       (__________.---
                      |
                 """,
                 "33": """
    SCISSORS                     SCISSORS
    _______           |           _______
---'   ____)____      |      ____(____   '---
          ______)     |     (______
       __________)    |    (_______
      (____)          |          (__
---.__(___)           |           (______.---
                      |
                 """}
        print(hands[combination])

    def print_result(self,result):
        """Prints the result's message.

        Args:
            result (string): the result represented by a letter.            
        """
        messages = {"w": "You win!",
        "d": "It's a draw!",
        "l": "You lose!"}

        print(messages[result])

    def print_current_score(self,player_score, ai_score,wins):
        """Prints the score of both the player and the Ai

        Args:
            player_score (int): the player's score. 
            ai_score (int): the ai's score.
            wins (int): The amount of wins to win the game      
        """
        print(f"\nSCORE: YOU {player_score}/{wins} - AI {ai_score}/{wins}")

    def print_final_result(self,final_result):
        """Prints the final result's message
        
        Args:
            final_result (string): The final result represented by a letter. 
               
        """
        messages = {"w":"\nCongragulations! you win!",
        "l": "\nToo bad! You lose!"}
        print(messages[final_result])