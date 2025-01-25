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
