import os
import sys
from core.services.learning_tracker import show_menu, add_day

sys.path.append(os.path.abspath("core"))

from models.tracker import Tracker

trackers = []

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Choose option: ").strip().lower()
        if choice == "1":
            add_day()
        elif choice == "q":
            print("Bye!")
            break
        else:
            print("Option not implemented yet.")



