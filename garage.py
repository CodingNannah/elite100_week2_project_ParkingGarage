class ParkingGarage(): 

    def __init__(self, stalls):
        self.name = "Coding Nannah's Honor System Parking Garage"
        self.spaces = list(range(1, stalls + 1))
        self.tickets = self.spaces[:]
        self.parkingSpaces = self.spaces
        # personal ticket not paid, yet. set to False:
        self.currentTicket = {"paid": False}


# enter (take ticket) - decrease ticket & spaces by 1; personal ticket ("false")

    def takeTicket(self):
        print(f"\nWelcome to {self.name}! Please park in the designated stall that's printed on your ticket.")
        for tickets in self.tickets:
            tickets -= 1
        for parkingSpaces in self.parkingSpaces:
            parkingSpaces -= 1


# pay (pay & receive msg) - personal ticket ("true") 

    def payParking(self):
        time = input("\nThe time-stamp on your ticket is when you entered. Exactly how many minutes were you parked? ")
        if int(time) >= 0:
            price = int(time) * 0.5
            print(f"Your ticket price is ${price:.2f}.")
            paidUp = input(f"Please type in {price:.2f} to pay. ")
            print("\nThank you for paying! You may now choose to leave.")
            if paidUp:
                # personal ticket paid! set to True
                self.currentTicket["paid"] = True
            else:
                print(f"Please enter {price:.2f} to pay and leave.")
        else:
            print("Please enter a whole number for the minutes you've parked. \
                You may enter 0 if you took a ticket and are leaving without parking.")    


# leave (paid & receive msg) - increase ticket & spaces by 1; 

    def leaveGarage(self):
        if self.currentTicket["paid"]:
            for tickets in self.tickets:
                tickets += 1
            for parkingSpaces in self.parkingSpaces:
                parkingSpaces += 1
            # 15 min to leave is too long!
            print(f"\nThank you for visiting {self.name}! You have 10 minutes to leave. You may exit safely to your right.") 
            print("Choose and type 'quit' to exit the program. ")  
        else:
            self.payParking()


# run the program!! 

    def run(self):
        print(f"""\n
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   You are visiting {self.name}!
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""")
        while True:
            response = input("\nChoose and type only one activity: park, pay, leave, or quit. ")
            response = response.strip().lower()

            if response == 'park':
                self.takeTicket()
            elif response == 'pay':
                self.payParking()
            elif response == 'leave':
                self.leaveGarage()    
            elif response == 'quit':
                print(f"Thanks for visiting {self.name}! Have a wonderful day!")
                break
            else:
                print("That didn't work. Please try again!")


garage = ParkingGarage(20)
garage.run()