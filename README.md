# EDP_System_Lectures


Here’s a more unique version of the provided description:

Event-Driven Hospital Workflow System

-This system is built around an event-driven architecture to simulate a hospital's workflow, using the observer design pattern. It facilitates seamless communication between various entities such as patients, doctors, pharmacies, and receptionists, triggered by events.

Key Components

-The system consists of the following essential parts:

1. Event: Represents a specific occurrence with its type and associated information, such as a patient's check-in or a medication request.
2. EventManager: Responsible for managing event subscriptions and distributing events to the appropriate listeners when they occur.
3. Patient: Simulates a hospital patient who can check in and request medications.
4. Doctor: Acts as a listener that responds to patient check-ins and medication requests, performing necessary actions like approving treatments.
5. Pharmacy: Listens for medication requests and handles the dispensing process for prescribed treatments.
6. Reception: Handles patient registrations upon check-in, ensuring all new arrivals are properly recorded.
