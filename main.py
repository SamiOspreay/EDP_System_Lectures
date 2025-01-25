class Event:
    def __init__(self, event_type, data):
        self.event_type = event_type
        self.data = data

class EventManager:
    def __init__(self):
        self.listeners = {}

    def register_listener(self, event_type, listener):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def dispatch(self, event):
        if event.event_type in self.listeners:
            for listener in self.listeners[event.event_type]:
                listener(event)


class Patient:
    def __init__(self, name, event_manager):
        self.name = name
        self.event_manager = event_manager

    def check_in(self):
        print(f"{self.name} is checking into the hospital.")
        event = Event("patient_check_in", {"name": self.name})
        self.event_manager.dispatch(event)

    def request_medication(self, medication):
        print(f"{self.name} is requesting medication: {medication}.")
        event = Event("medication_request", {"name": self.name, "medication": medication})
        self.event_manager.dispatch(event)