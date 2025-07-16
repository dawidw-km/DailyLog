from datetime import datetime

class Tracker:
    _id_counter = 1

    def __init__(self, created_at=None):
        self.id = Tracker._id_counter
        Tracker._id_counter += 1
        self.created_at = created_at if created_at is not None else datetime.now()
        self.information = []

    def add_information(self, title, description, time_learning):
        self.information.append({
            "title": title,
            "description": description,
            "time_learning": time_learning
        })

    def to_dict(self):
        return {
            "id": self.id,
            "created_at": self.created_at.date().isoformat(),
            "information": self.information   
        }

    @staticmethod
    def from_dict(data):
        created_at = datetime.fromisoformat(data["created_at"]) if "created_at" in data else None
        tracker = Tracker(
            created_at=created_at
        )
        data_information = data["information"]
        tracker.information = data_information
        tracker.id = data.get("id", tracker.id)
        Tracker._id_counter = max(Tracker._id_counter, tracker.id +1)
        return tracker

    def __str__(self):
        return (f"{self.created_at}\n, {self.information}")