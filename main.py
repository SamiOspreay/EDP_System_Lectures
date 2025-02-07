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

class Doctor:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        event_manager.register_listener("patient_check_in", self.attend_patient)
        event_manager.register_listener("medication_request", self.approve_medication)

    def attend_patient(self, event):
        print(f"Doctor: Attending to patient {event.data['name']}.")

    def approve_medication(self, event):
        print(f"Doctor: Approving medication {event.data['medication']} for {event.data['name']}.")

class Pharmacy:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        event_manager.register_listener("medication_request", self.dispense_medication)

    def dispense_medication(self, event):
        print(f"Pharmacy: Dispensing {event.data['medication']} for {event.data['name']}.")


class Reception:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        event_manager.register_listener("patient_check_in", self.register_patient)

    def register_patient(self, event):
        print(f"Reception: Registering patient {event.data['name']}.")

def main():
    event_manager = EventManager()

    
    patient1 = Patient("Patrycja", event_manager)
    patient2 = Patient("Tomek", event_manager)
    doctor = Doctor(event_manager)
    pharmacy = Pharmacy(event_manager)
    reception = Reception(event_manager)

    
    patient1.check_in()
    patient2.check_in()
    patient1.request_medication("Apap")
    patient2.request_medication("Ibuprom")

main()
