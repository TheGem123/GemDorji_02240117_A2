
import json
import os


class PokemonBinder:
    def __init__(self):
        self.cards = {}  # Stores {pokemon_number: page}
        self.save_file = "pokemon_binder.json"
        self.load_progress()

    def add_card(self, number):
        """Add a new Pokemon card to the collection"""
        if not 1 <= number <= 151:
            return "Please enter a number between 1-151"

        if number in self.cards:
            return f"You already have Pokemon #{number}!"

        # Calculate page (9 cards per page)
        page = (len(self.cards) // 9 + 1)
        self.cards[number] = page
        self.save_progress()

    def find_card(self, number):
        """Locate a specific Pokemon card"""
        if not 1 <= number <= 151:
            return "Please enter a valid Pokedex number (1-151)"

        if number not in self.cards:
            return f"Pokemon #{number} isn't in your collection yet"

        return f"Pokemon #{number} is on page {self.cards[number]}"

    def show_collection(self):
        """Display all collected cards"""
        if not self.cards:
            return "Your binder is empty. Start collecting!"

        # Group cards by page
        pages = {}
        for num, page in self.cards.items():
            pages.setdefault(page, []).append(num)

        # Create display text
        display = []
        for page in sorted(pages):
            cards = sorted(pages[page])
            display.append(f"Page {page}: " +
                           ", ".join(f"#{n}" for n in cards))

        # Add collection status
        collected = len(self.cards)
        status = f"\n\nProgress: {collected}/151 Pokemon"
        if collected == 151:
            status += "\nCongratulations! You've caught them all!"

        return "\n".join(display) + status

    def reset(self):
        """Clear all collected cards"""
        self.cards = {}
        if os.path.exists(self.save_file):
            os.remove(self.save_file)

    def save_progress(self):
        """collections saved to file"""
        with open(self.save_file, 'w') as f:
            json.dump(self.cards, f)

    def load_progress(self):
        # Loads previous collection from the file
        ''' if os.path.exists(self.save_file):
             with open(self.save_file, 'r') as f:
                 self.cards = {int(k): v for k, v in json.load(f).items()}'''
        if os.path.exists(self.save_file):
            with open(self.save_file) as f:
                saved_data = json.load(f)
                self.cards = {int(id): details for id,
                              details in saved_data.items()}


def main():
    print("Welcome to your Pokemon Card Binder!")
    binder = PokemonBinder()

    while True:
        print("\nWhat would you like to do?")
        print("1. Add a Pokemon card")
        print("2. View your collection")
        print("3. Find a Pokemon current location")
        print("4. Start over")
        print("5. Exit the program")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            try:
                num = int(input("kindly enter Pokemon number (1-151): "))
                result = binder.add_card(num)
                if result:
                    print(result)
                else:
                    print(f"Added Pokemon #{num} to your binder!")
            except ValueError:
                print("Kindly enter a number between 1-151")

        elif choice == '2':
            print("\n" + binder.show_collection())

        elif choice == '3':
            try:
                num = int(input("Which Pokemon are you looking for? (1-151): "))
                print("\n" + binder.find_card(num))
            except ValueError:
                print("Kindly enter a valid number")

        elif choice == '4':
            if input("would you like to reset the program? (y/n): ").lower() == 'y':
                binder.reset()
                print("Your binder has been cleared.")

        elif choice == '5':
            print("Thank you for spending time Pokemon Card Binder!")
            break

        else:
            print("Please choose a number between 1-5")


if __name__ == "__main__":
    main()
