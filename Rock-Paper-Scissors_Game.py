import random

class RockPaperScissorsGame:
    def __init__(self):
        self.choices = ["Rock", "Paper", "Scissors"]
        self.results = {
            ("Rock", "Paper"): "Computer wins!",
            ("Paper", "Rock"): "You win!",
            ("Scissors", "Paper"): "You win!",
            ("Paper", "Scissors"): "Computer wins!",
            ("Rock", "Scissors"): "You win!",
            ("Scissors", "Rock"): "Computer wins!",
        }

    def play(self):
        while True:
            user_choice = self.get_user_choice()
            computer_choice = random.choice(self.choices)

            print("You chose:", user_choice)
            print("Computer chose:", computer_choice)

            result = self.calculate_winner(user_choice, computer_choice)
            print(result)

            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                break

    def get_user_choice(self):
        while True:
            user_choice = input("Choose Rock, Paper, or Scissors: ")
            if user_choice in self.choices:
                return user_choice
            else:
                print("Invalid choice. Please choose Rock, Paper, or Scissors.")

    def calculate_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        return self.results.get((user_choice, computer_choice), "Computer wins!")

# Create an instance of the game and start playing
game = RockPaperScissorsGame()
game.play()
