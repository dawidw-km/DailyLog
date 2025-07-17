import os
from core.models.tracker import Tracker
from utils.storage import save_tracker_to_file, load_tracker_from_file
import sys
sys.path.append("~/VSC/Learning_tracker/core/models")

trackers = load_tracker_from_file()

##Shows menu
def show_menu():
    os.system("clear")  ## Clear terminal
    print("1.Add new day.")
    print("2.Edit your day.")
    print("3.Show latest day.")
    print("4.Show months.")
    print("q.Quit")

## Validates Title
def validated_information_title():
    while True:
        try:
            title = input("Set title\nType: ").strip().lower()
            if not title or len(title) > 100:
                raise ValueError("Title cannot be empty or longer than 100 characters.")
            for tracker in trackers:
                for info in tracker.information:
                    if info['title'].lower() == title:
                        raise ValueError("Title already exists.")
                
            return title
        except ValueError as e:
            print(f"Error: {e}")

## Validates Description
def validated_information_description():
    while True:
        try:
            description = input("Add description\nType: ")
            if not description or len(description) > 3000:
                raise ValueError("Description cannot be empty or longer than 3000 characters.")
            return description
        except ValueError as e:
            print(f"Error: {e}")

    ##Validates Time spent
def validated_time_spent():
    while True:
        try:
            time_learning = int(input("How much time did you spent in minutes?: "))
            if time_learning > 1440 or time_learning < 0:
                raise ValueError("Try less than 1440(24 hours) and cannot be a negative number.")
            return time_learning
        except ValueError as e:
            print(f"Error: {e}. Enter a valid number.")

# Adds new day
def add_day():
    title_items = []
    description_items = []
    time_learning_list = []
    while True:
        title = validated_information_title()
        title_items.append(title)
        description = validated_information_description()
        description_items.append(description)
        time_learning = validated_time_spent()
        time_learning_list.append(time_learning)
        ask_to_continue = input("Do you want to add another one?\nType y/n:").strip().lower()
        if ask_to_continue == "y":
            continue
        elif ask_to_continue == "n":
            break

    tracker = Tracker()
    for title, description, time_learning in zip(title_items, description_items, time_learning_list):
        tracker.add_information(title, description, time_learning)
    trackers.append(tracker)
    save_tracker_to_file(trackers)

def edit_day():
    while True:
        latest_day = max(trackers, key=lambda t: t.id)
        print(latest_day)
        x = input("q")
        if x == 'q':
            break