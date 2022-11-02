Python Object-Oriented (OOP) Parking Garage

Project Week 2 Assignment:
Create a Parking Garage Class to get more familiar with OOP.

Your parking garage class should have the following methods:
- takeTicket
    - This should decrease the amount of tickets available by 1
    - This should decrease the amount of parkingSpaces available by 1
- payForParking
    - Display an input that waits for an amount from the user and store it in a variable
    - If the payment variable is not empty (meaning the ticket has been paid), then -> display a message to the user that their ticket has been paid and they have 15mins to leave
    - This should update the "currentTicket" dictionary key "paid" to True
-leaveGarage
    - If the ticket has been paid, display a message of "Thank You! Have a nice day."
    - If the ticket has not been paid, display an input prompt for payment
        - Once paid, display message "Thank you, have a nice day!"
    - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
    - Update tickets list to increase by 1 (meaning add to the tickets list)

You will need a few attributes as well:
- tickets -> list
- parkingSpaces -> list
- currentTicket -> dictionary

By the end of this project, the student should be able to:
- Explain and/or demonstrate creating classes
- Explain and/or demonstrate creating methods
- Explain and/or demonstrate creating instantiation

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Personal Notes:
# set up class
    # attributes == characteristics (as function parameters)
        # arguments == the specifics (calling the parameters of the function)
    # methods == actions
    # instantiation == __init__ and other methods (functions of objects)
    # objects == variables assigned to classes
    # remember SELF! == current instance of class

# future: figure out how to do this for ANY size garage!
# 15 minutes to leave is too much time for such a small location. Reducing it to 10 min.