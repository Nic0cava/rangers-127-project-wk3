




























# WELCOME TO OUR GARAGE 
# welcome to the garage
# print("\nWelcome to the OOP Car Garage")
# print("Open in 2023 by Priscilla and Nico")
# #display the car garage info and prices
# print("\n\t------------| Hourly fees and fines |-------------")
# print("\t Hourly fee: $10.00 | TIME STARTS NOW \n\t | IF PARKED OVER 24 HOURS fee is $100.00 | n\t PLEASE PAY BEFORE EXITING GARAGE |")


# #
class Car():
    def __init__(self, license_plate, make, color):
        self.license_plate = license_plate
        self.make = make
        self.color = color

    def print_car(self):
        print("Car info:")
        print(f"License Plate: {self.license_plate}, Make: {self.make}, Color: {self.color}")

class Parking():

    def __init__(self, tickets, parking_spaces, customer_ticket):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.customer_ticket = customer_ticket

    def available_spots(self):
        print(f"\nParking spots available: {self.parking_spaces}")

    def take_ticket():
        self.customer_ticket += 1
        self.tickets -= 1
        self.parking_spaces -= 1

    def pay_ticket():
        pass

    def return_ticket():
        pass


print("\nWelcome to the OOP Car Garage")
print("Open in 2023 by Priscilla and Nico")
#display the car garage info and prices
print("\n\t------------| Hourly fees and fines |-------------")
print("\t Hourly fee: $10.00 | TIME STARTS NOW \n\t | IF PARKED OVER 24 HOURS fee is $100.00 | \n\t |PLEASE PAY BEFORE EXITING GARAGE |")

p = Parking(25, 25, 0)
p.available_spots()
lp = input("Enter your license plate: ").upper()
make = input("Enter make of car: ").title()
color = input("Enter color of car: ").lower()
c = Car(lp, make, color)
c.print_car()



# The Initial Driver needs to Make sure to:
# download the files below, create a local folder for the project, create a github repository, commit the inital files, share the link

# Both navigators should then:
# fork the code, clone it and begin.

# Here's an article on doing so -- https://stackoverflow.com/questions/3903817/pull-new-updates-from-original-github-repository-into-forked-github-repository

# Your parking gargage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary