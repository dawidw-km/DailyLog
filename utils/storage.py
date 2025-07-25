import json
from core.models.tracker import Tracker

filename = "C:/Users/Dawid/Documents/VSC/DailyLog/data/tracker.json"


def save_tracker_to_file(trackers):
    with open(filename, "w") as f:
        json.dump([tracker.to_dict() for tracker in trackers], f, indent=4)

def load_tracker_from_file():
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            if not data:
                Tracker._id_counter = 1
                return []
            return [Tracker.from_dict(tracker_dict) for tracker_dict in data]
    except FileNotFoundError:
        Tracker._id_counter = 1
        return []
    except json.JSONDecodeError:
        ("File empty or incorrect format")
        return []