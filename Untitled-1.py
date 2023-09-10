class ParkingGarage:
    def __init__(self, total_spaces):
        self.tickets = [i for i in range(1, total_spaces + 1)]
        self.parkingSpaces = [i for i in range(1, total_spaces + 1)]
        self.currentTicket = {}

    def takeTicket(self):
        if self.tickets:
            ticket = self.tickets.pop()
            parking_space = self.parkingSpaces.pop()
            self.currentTicket[ticket] = {"paid": False, "parking_space": parking_space}
            print(f"Your ticket number is {ticket}. Please park in space {parking_space}.")
        else:
            print("Sorry, the garage is full. No tickets available.")

    def payForParking(self, ticket):
        if ticket in self.currentTicket and not self.currentTicket[ticket]["paid"]:
            amount = input("Please enter the payment amount: ")
            if amount:
                self.currentTicket[ticket]["paid"] = True
                print("Thank you for your payment. You have 15 minutes to leave.")
            else:
                print("Payment is required to exit the garage.")
        else:
            print("Invalid ticket or ticket already paid.")

    def leaveGarage(self, ticket):
        if ticket in self.currentTicket:
            if self.currentTicket[ticket]["paid"]:
                print("Thank you, have a nice day!")
            else:
                while True:
                    amount = input("Please pay for your ticket before leaving: ")
                    if amount:
                        self.currentTicket[ticket]["paid"] = True
                        print("Payment accepted. Thank you, have a nice day!")
                        break
                    else:
                        print("Payment is required to exit the garage.")
            self.parkingSpaces.append(self.currentTicket[ticket]["parking_space"])
            self.tickets.append(ticket)
            del self.currentTicket[ticket]
        else:
            print("Invalid ticket number.")

# Usage example:
if __name__ == "__main__":
    garage = ParkingGarage(10)  # Create a parking garage with 10 spaces
    while True:
        print("\nOptions:")
        print("1. Take a ticket")
        print("2. Pay for parking")
        print("3. Leave the garage")
        print("4. Exit")
        choice = input("Select an option (1/2/3/4): ")

        if choice == "1":
            garage.takeTicket()
        elif choice == "2":
            ticket = int(input("Enter your ticket number: "))
            garage.payForParking(ticket)
        elif choice == "3":
            ticket = int(input("Enter your ticket number: "))
            garage.leaveGarage(ticket)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")