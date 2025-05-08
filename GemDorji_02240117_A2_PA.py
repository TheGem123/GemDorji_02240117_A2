import random


class GameCollection:
    def __init__(self):
        self.scores = {
            "Guess the Number": 0,
            "rock_paper_scissors_game": 0,
            "Trivia Pursuit Game": 0,
            "pokemon_card_binder_manager": 0
        }

    def display_menu(self):
        """Show the game menu"""
        print("\n1.Guess the Number ")
        print("2. rock_paper_scissors_game")
        print("3. Trivia Pursuit Game")
        print("4.pokemon_card_binder_manager")
        print("5. View Overall Scores")
        print("6. Exit the program")
        return input("Choose a game (1-5): ")

    def guess_the_number(self):
        """Simple number guessing game"""
        print("\n=== Try your luck! ===")
        secret = random.randint(1, 50)
        attempts = 0

        while True:
            try:
                guess = int(input("Guess a number between 1-50: "))
                attempts += 1

                if guess < secret:
                    print("Too low!")
                elif guess > secret:
                    print("Too high!")
                else:
                    print(f"Correct! You guessed it in {attempts} tries!")
                    self.scores["Guess the Number"] += 1
                    break
            except ValueError:
                print("Please enter a valid number!")

    def rock_paper_scissors_game(self):
        options = ["rock", "paper", "scissors"]
        beats = {
            "rock": "scissors",    # Rock beats scissors
            "paper": "rock",       # Paper beats rock
            "scissors": "paper"    # Scissors beat paper
        }

        while True:
            # Get player's move
            player_move = input("choose rock, paper, or scissors: ").lower()
            while player_move not in options:
                print("error! kindly pick rock, paper, or scissors.")
                player_move = input(
                    "choose rock, paper, or scissors: ").lower()

            # Computer selects random choice
            computer_move = random.choice(options)
            print(f"\nYou played: {player_move}")
            print(f"Computer played: {computer_move}")

            # Display the result
            if player_move == computer_move:
                print("It's a draw!")
            elif beats[player_move] == computer_move:
                print("Congrats you beat the computer! 🎉")
                break
            else:
                print("Oops! Computer wins!")

            print()  # Empty line for spacing

    def trivia_Pursuit_game(self):
        """Simple trivia game with 3 questions"""
        print("\n=== Trivia_Pursuit_Game ===")

        Quiz_data = [
            {
                "question": "What is the capital of Bhutan?",
                "choices": ["Thimphu", "Trongsa", "Bumthang", "Wangdue"],
                "ans": "Thimphu"
            },
            {
                "question": "How many continents are there?",
                "choices": ["5", "6", "7", "8"],
                "ans": "7"
            },
            {
                "question": "What is 2 + 2?",
                "choices": ["3", "4", "5", "6"],
                "ans": "4"
            }
        ]

        for question in Quiz_data:
            print("\n" + question["question"])
            for i, choices in enumerate(question["choices"], 1):
                print(f"{i}. {choices}")

            while True:
                answer = input("Your ans (1-4): ")
                if answer in ["1", "2", "3", "4"]:
                    break
                print("Please enter 1, 2, 3, or 4")

            if question["choices"][int(answer)-1] == question["ans"]:
                print("Correct!")
                self.scores["Trivia Pursuit Game"] += 1
            else:
                print(f"Wrong! The ans was: {question['ans']}")

    def pokemon_card_binder_manager(self):
        print("Welcome to Pokemon Card Binder Manager!")
        print("Main Menu:")
        print("1. Add Pokemon card")
        print("2. Reset Binder")
        print("3. View Current placements")
        print("4. Exit")

    def view_Overall_scores(self):
        """Show the current scores"""
        print("\n=== YOUR SCORES ===")
        for game, score in self.scores.items():
            print(f"{game}: {score} wins")

    def run(self):
        """Main program loop"""
        print("Welcome to Simple Fun Game!")

        while True:
            choice = self.display_menu()

            if choice == "1":
                self.guess_the_number()
            elif choice == "2":
                self.rock_paper_scissors_game()
            elif choice == "3":
                self.trivia_Pursuit_game()
            elif choice == "4":
                self.pokemon_card_binder_manager()
            elif choice == "5":
                self.view_Overall_scores()
            elif choice == "6":
                print("Thanks for playing!")
                break
            else:
                print("Please enter a number between 1-6")


# Run the game collection
if __name__ == "__main__":
    game_collection = GameCollection()
    game_collection.run()
