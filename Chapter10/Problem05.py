# Write a Class ‘Train’ which has methods to book a ticket,
# get status (no of seats) and get fare information of train
# running under Bangladesh Railways.


class Train:

    @staticmethod
    def greet():
        print("Hello, Sir/Mam.")

    def __init__(self):
        self.total_seats = 500
        self.available_seats = 500

    def ticket(self):
        if self.available_seats == 0:
            print("Sorry, No ticket available")
            return False

        print("Ticket available")
        y = input("Do you want to book? ").lower()

        if y == "yes":
            print("Ticket Booked")
            self.available_seats -= 1
            return True
        else:
            print("Thank You for using our service")
            return False

    def seat(self):
        print(f"Total seats: {self.total_seats}")
        print(f"Total seats available: {self.available_seats}")

    def price(self):
        print("You are currently in Dhaka.")
        print("Where do you want to go?")

        location = input(
            "01. Sylhet\n"
            "02. Rangpur\n"
            "03. Chittagong\n"
            ": "
        ).lower()

        if location == "sylhet":
            print("Ticket price is 250 TAKA")
        elif location == "chittagong":
            print("Ticket price is 500 TAKA")
        elif location == "rangpur":
            print("Ticket price is 450 TAKA")
        else:
            print("Sorry, No route is available for now")


# Start program
Train.greet()

a = Train()

result = a.ticket()

if result == True:
    a.seat()
    a.price()
else:
    print("Good Bye")
