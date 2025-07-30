# Source code for adventure_game.py
print("Welcome to the Adventure Game!")

def forest_path():
    print("\nThe forest is dense and mysterious. You hear the sound of running water nearby.")
    print("Do you want to:")
    print("1. Follow the river")
    print("2. Climb a tree to get a better view")
    choice = input("Enter 1 to follow the river or 2 to climb the tree: ")
    if choice == "1":
        print("\nYou follow the river and discover a hidden waterfall. Behind it, you find a secret cave!")
        print("Congratulations! You are one step closer to the treasure.")
        # You can add more story or call cave_path() here
    elif choice == "2":
        print("\nYou climb the tree and spot a clearing with strange markings on the ground.")
        print("Suddenly, the branch breaks and you fall, but you find a mysterious map on the ground.")
        print("The map leads you toward the treasure!")
        # You can add more story or next steps here
    else:
        print("\nInvalid choice. Please try again.")
        forest_path()

# ...existing code...

def cave_path():
    print("\nThe cave is cold and echoing. You can barely see anything inside.")
    print("Do you want to:")
    print("1. Light a torch")
    print("2. Proceed in the dark")
    choice = input("Enter 1 to light a torch or 2 to proceed in the dark: ")
    if choice == "1":
        print("\nWith the torch lit, you see ancient carvings on the walls and safely navigate deeper.")
        print("You discover a chest filled with gold and jewels. You found the legendary treasure!")
        print("Congratulations, you win!")
    elif choice == "2":
        print("\nYou stumble in the darkness and fall into a pit. Your adventure ends here.")
        print("Game Over. Better luck next time!")
    else:
        print("\nInvalid choice. Please try again.")
        cave_path()

# ...existing code...
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
        forest_path()
    elif choice == "2":
        print("\nYou step into the mysterious cave...")
        cave_path()  # Call the cave_path function here
    else:
        print("\nInvalid choice. Please try again.")
        start_game()

# ...existing code...
# Call the function to start the game
start_game()