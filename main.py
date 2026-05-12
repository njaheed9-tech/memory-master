"""
main.py - Entry point for MemoryMaster.

Run this file to start the game:
    python main.py
"""

from game import MemoryMasterGame


def get_mode():
    """
    Ask the player to pick a game mode and return their choice.

    Returns:
        str: 'numbers', 'phrases', or 'pictures'
    """
    print("\n" + "=" * 40)
    print("CHOOSE A GAME MODE")
    print("=" * 40)
    print("1. Numbers - Remember a sequence of digits")
    print("2. Phrases - Remember a list of words in order")
    print("3. Pictures - Remember an ASCII pattern")
    print("-" * 40)
    
    while True:
        try:
            choice = input("Enter 1, 2, or 3: ").strip()
            if choice == "1":
                print("\n✓ Numbers mode selected\n")
                return "numbers"
            elif choice == "2":
                print("\n✓ Phrases mode selected\n")
                return "phrases"
            elif choice == "3":
                print("\n✓ Pictures mode selected\n")
                return "pictures"
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            exit()


def get_difficulty():
    """
    Ask the player to pick a difficulty and return their choice.

    Returns:
        str: 'easy', 'medium', or 'hard'
    """
    print("\n" + "=" * 40)
    print("CHOOSE A DIFFICULTY")
    print("=" * 40)
    print("1. Easy (5 seconds to memorize)")
    print("2. Medium (3 seconds to memorize)")
    print("3. Hard (1.5 seconds to memorize)")
    print("-" * 40)
    
    while True:
        try:
            choice = input("Enter 1, 2, or 3: ").strip()
            if choice == "1":
                print("\n✓ Easy mode selected - Good luck!\n")
                return "easy"
            elif choice == "2":
                print("\n✓ Medium mode selected - You've got this!\n")
                return "medium"
            elif choice == "3":
                print("\n✓ Hard mode selected - Challenge accepted!\n")
                return "hard"
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            exit()


if __name__ == "__main__":
    mode = get_mode()
    difficulty = get_difficulty()
    
    game = MemoryMasterGame(mode=mode, difficulty=difficulty)
    game.run()