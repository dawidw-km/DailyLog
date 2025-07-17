import os
import sys
from core.services.learning_tracker import show_menu, add_day, edit_day
from utils.storage import save_tracker_to_file, load_tracker_from_file

sys.path.append(os.path.abspath("core"))

from models.tracker import Tracker

trackers = []

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Choose option: ").strip().lower()
        if choice == "1":
            add_day()
        elif choice == "2":
            edit_day()
        elif choice == "q":
            print("Bye!")
            break



