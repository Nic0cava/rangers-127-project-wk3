#_________PSUEDO CODE__________
# comments will go here (updated 8/18 @ 1 PM EST)
# Created by Priscilla and Nico

# WELCOME TO OUR OOP GARAGE 

# there are 25 spots available spots in our parking lot 
# it costs $10 an hour to park in this garage #
# if you car is parked for 24 hours or more you will be charged a $100 fine

# OUR CLASSES 

# car class 
    #car info
    #track the time we parked at
    # tracks license plate #'s
    # make of vehicle 
    #color of vehicle 

#parking class
    # counts # of parking spots left 
    # labeled parking spots 


# WELCOME TO OUR GARAGE 
print("\nWelcome to the OOP Car Garage")
print("Opened in August 2023 by Priscilla and Nico")
#display the car garage info and prices
print("\n\t------------| Hourly fees and fines |-------------")
print("\t Hourly fee: $10.00 | TIME STARTS NOW \n\t | IF PARKED OVER 24 HOURS fee is $100.00 | \n\t |  PLEASE PAY BEFORE EXITING GARAGE      |")

class Car():
    def __init__(self, license_plate, make, color):
        self.license_plate = license_plate
        self.make = make
        self.color = color

    def print_car(self):
        print("Car info:")
        print(f"License Plate: {self.license_plate}, Make: {self.make}, Color: {self.color}")

class Parking():

    def __init__(self):
        self.garage = {'spots' : 25 , 'tickets': 0}
        self.ticket = {}
        self.ticketid = ['1A', '2B', '3C', '4D' , '5E', '6F', '7G' , '8H', 
                         '9I', '10J', '11K', '12L', '13M' , '14N', '15O', '16P',
                          '17Q','18R','19S','20T','21U' ,'22V', '23W' ,'24X', '25Y']
        self.cars_added = []
        total_customers = []

    def available_spots(self):
        print(f"\nParking spots available: {self.garage['spots']}")

    def take_ticket(self, car):
        self.garage['spots'] -= 1
        self.garage['tickets'] += 1
        self.ticketid = ['1A', '2B', '3C', '4D' , '5E', '6F', '7G' , '8H', 
                         '9I', '10J', '11K', '12L', '13M' , '14N', '15O', '16P',
                          '17Q','18R','19S','20T','21U' ,'22V', '23W' ,'24X', '25Y']
    
        return self.garage


 


    # def add_cars(self,car):

    # def pay_ticket():
    #     pass  


    def return_ticket(self):
        self.garage['spots'] += 1
        self.garage['tickets'] -= 1
        return f"Thank You, have a nice day"

p = Parking()
p.available_spots()
lp = input("Enter your license plate: ").upper()
make = input("Enter make of car: ").title()
color = input("Enter color of car: ").lower()
c = Car(lp, make, color)
c.print_car()


print(p.take_ticket())



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