#1. City Infrastructure Management System
#Task 1. Vehicle Registration System
class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.registration_number = reg_num
        self.type = vehicle_type
        self.owner = owner


    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"The owner of vehicle {self.registration_number} has been updated to {self.owner}")



#2. Task 2: Event Management System Enhancement
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1
        print(f"Participant added to event {self.name}. Total participants: {self.participant_count}")

    def get_participant_count(self):
        return self.participant_count





if __name__ == "__main__":
    # Creating instances of Vehicle
    vehicle1 = Vehicle("ABC123", "Car", "John Doe")
    vehicle2 = Vehicle("XYZ789", "Truck", "Jane Smith")

    # Display initial state of vehicles
    print(f"Vehicle 1 - Registration Number: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
    print(f"Vehicle 2 - Registration Number: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")

    # Updating the owner of vehicle1
    vehicle1.update_owner("Alice Johnson")
    # Updating the owner of vehicle2
    vehicle2.update_owner("Bob Brown")

    # Display updated state of vehicles
    print(f"Vehicle 1 - Registration Number: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
    print(f"Vehicle 2 - Registration Number: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")

    event = Event("City Marathon", "2024-07-15")

    # Display initial participant count
    print(f"Initial participant count for {event.name}: {event.get_participant_count()}")

    # Adding participants
    event.add_participant()
    event.add_participant()
    event.add_participant()

    # Display updated participant count
    print(f"Updated participant count for {event.name}: {event.get_participant_count()}")

