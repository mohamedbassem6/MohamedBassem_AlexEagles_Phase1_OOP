from flight_system import FlightSystem
import utils

sys = FlightSystem()

utils.populate(sys)
utils.prompt_customer(sys)

print("\nWelcome to the Flight Booking System!")
while True:
    print()
    print("1. Search Flights")
    print("2. Book Ticket")
    print("3. View Tickets")
    print("4. View Airlines")
    print("5. View Airports")
    print("6. Log Out")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        utils.prompt_search(sys)
    elif choice == 2:
        utils.prompt_book(sys)
    elif choice == 3:
        utils.view_tickets(sys)
    elif choice == 4:
        utils.view_airlines(sys)
    elif choice == 5:
        utils.view_airports(sys)
    elif choice == 6:
        sys.logout_customer()
        print("\nLogged out successfully!\n")
        utils.prompt_customer(sys)
    