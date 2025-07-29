# Source code for adventure_game.py
print("Welcome to the Adventure Game!")

def start_game():
    print("\nYour quest: Find the legendary treasure hidden in the ancient land!")
    name = input("What is your name, brave explorer? ")
    print(f"\nWelcome, {name}! Your adventure begins now.")
    print("You stand at a crossroads. Do you want to:")
    print("1. Explore the dark forest")
    print("2. Enter the mysterious cave")
    choice = input("Enter 1 for forest or 2 for cave: ")
    if choice == "1":
        print("\nYou head into the dark forest...")
        # forest_path() will be called here in Task 3
    elif choice == "2":
        print("\nYou step into the mysterious cave...")
        # cave_path() will be called here in Task 4
    else:
        print("\nInvalid choice. Please try again.")
        start_game()

# Call the function to start the game
start_game()