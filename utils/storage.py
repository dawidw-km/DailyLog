import json
from core.models.tracker import Tracker

filename = "data/tracker.json"

def save_tracker_to_file(trackers):
    with open(filename, "w") as f:
        json.dump([tracker.to_dict() for tracker in trackers], f, indent=4)

def load_tracker_from_file():
    pass

