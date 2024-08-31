from flight_system import FlightSystem, Airline, Airport, Flight, Customer, Ticket
from datetime import datetime
import random

def populate(sys: FlightSystem):
    sys.add_airline(Airline("Egypt Air"))
    sys.add_airline(Airline("Wizz Air"))
    sys.add_airline(Airline("Air Cairo"))
    sys.add_airline(Airline("American Airlines"))
    sys.add_airline(Airline("Delta Air Lines"))
    sys.add_airline(Airline("United Airlines"))
    sys.add_airline(Airline("Lufthansa"))
    sys.add_airline(Airline("Emirates"))
    sys.add_airline(Airline("Qatar Airways"))
    sys.add_airline(Airline("British Airways"))
    sys.add_airline(Airline("Air France"))
    sys.add_airline(Airline("Singapore Airlines"))

    sys.add_airport(Airport("Cairo International Airport", "Cairo", "Egypt"))
    sys.add_airport(Airport("Heathrow Airport", "London", "United Kingdom"))
    sys.add_airport(Airport("Hartsfield-Jackson Atlanta International Airport", "Atlanta", "United States"))
    sys.add_airport(Airport("Beijing Capital International Airport", "Beijing", "China"))
    sys.add_airport(Airport("Dubai International Airport", "Dubai", "United Arab Emirates"))
    sys.add_airport(Airport("Los Angeles International Airport", "Los Angeles", "United States"))
    sys.add_airport(Airport("Tokyo Haneda Airport", "Tokyo", "Japan"))

    sys.add_flight(
        Flight(
            1,
            sys.get_airline("Egypt Air"),
            sys.get_airport("Cairo International Airport"),
            sys.get_airport("Heathrow Airport"),
            datetime(2024, 1, 1, 10, 30),
            500,
        )
    )

    sys.add_flight(
        Flight(
            2,
            sys.get_airline("Wizz Air"),
            sys.get_airport("Cairo International Airport"),
            sys.get_airport("Dubai International Airport"),
            datetime(2024, 1, 2, 12, 30),
            300,
        )
    )

    sys.add_flight(
        Flight(
            3,
            sys.get_airline("Lufthansa"),
            sys.get_airport("Dubai International Airport"),
            sys.get_airport("Los Angeles International Airport"),
            datetime(2024, 1, 3, 14, 30),
            700,
        )
    )

    sys.add_flight(
        Flight(
            4,
            sys.get_airline("American Airlines"),
            sys.get_airport("Hartsfield-Jackson Atlanta International Airport"),
            sys.get_airport("Beijing Capital International Airport"),
            datetime(2024, 1, 4, 16, 30),
            600,
        )
    )

    sys.add_flight(
        Flight(
            5,
            sys.get_airline("British Airways"),
            sys.get_airport("London Heathrow Airport"),
            sys.get_airport("Tokyo Haneda Airport"),
            datetime(2024, 1, 5, 18, 30),
            800,
        )
    )


def prompt_customer(sys: FlightSystem):
    print("\nEnter your details to book a ticket\n")
    name = input("Enter your name: ")
    while not name.strip():
        print("\nName cannot be empty!")
        name = input("Enter your name: ")

    age = input("Enter your age: ")
    while not age.strip() or int(age) < 0:
        print("\nPlease enter a valid age!")
        age = input("Enter your age: ")

    age = int(age)

    gender = input("Enter your gender (M/F): ")
    while not gender.strip() or gender.capitalize() not in ["M", "F"]:
        print("\nPlese enter a valid answer!")
        gender = input("Enter your gender (M/F): ")

    nationality = input("Enter your nationality: ")
    while not nationality.strip():
        print("\nNationality cannot be empty!")
        nationality = input("Enter your nationality: ")

    sys.login_customer(Customer(name, age, gender.capitalize(), nationality))


def prompt_search(sys: FlightSystem):
    print("\nSearch for a flight\nLeave blank to skip a field\n")

    search_keys = dict()
    
    flight_no = input("Enter the flight number: ")
    if flight_no.strip():
        search_keys["flight_no"] = int(flight_no)

    airline = input("Enter the airline: ")
    if airline.strip():
        search_keys["airline"] = sys.get_airline(airline)

    departure = input("Enter the departure airport/city/country: ")
    if departure.strip():
        search_keys["departure_airport"] = sys.get_airport(departure)

    destination = input("Enter the destination airport/city/country: ")
    if destination.strip():
        search_keys["arrival_airport"] = sys.get_airport(destination)

    date = input("Enter the day (YYYY-MM-DD): ")
    if date.strip():
        search_keys["date"] = datetime.strptime(date, "%Y-%m-%d")

    price = input("Enter the price: ")
    if price.strip():
        search_keys["price"] = float(price)

    if len(search_keys) == 0:
        print("\nNo search criteria provided!\n")
    else:
        response = sys.search_flights(search_keys)
        if not response:
            print("\nNo flights found!\n")
        else:
            print("\nSearch Results\n")

        for flight in response:
            print()
            print(f"Flight number: {flight.get_flight_number()}")
            print(f"Airline: {flight.get_airline().get_name()}")
            print(f"Departure: {flight.get_departure_airport().get_name()}")
            print(f"Destination: {flight.get_arrival_airport().get_name()}")
            print(f"Time: {flight.get_time().strftime("%Y-%m-%d %I:%M %p")}")
            print(f"Price: {flight.get_price()}")



def prompt_book(sys: FlightSystem):
    print("\nBook a ticket\n")

    customer = sys.get_customer()

    flight_no = int(input("Enter the flight number: "))
    flight = sys.get_flight(flight_no)
    if not flight:
        print("\nFlight not found!\n")
        return
    
    meal_type = input("Enter your meal type (Chicken/Beef): ")
    while meal_type.capitalize() not in ["Chicken", "Beef"]:
        print("\nPlease enter a valid meal type!")
        meal_type = input("Enter your meal type (Chicken/Beef): ")

    ticket = Ticket(flight, random.randint(1, 250), meal_type)
    customer.book_ticket(ticket)

    print("\nTicket booked successfully!\n")


def view_tickets(sys: FlightSystem):
    customer = sys.get_customer()
    tickets = customer.get_tickets()

    if not tickets:
        print("\nNo tickets found!\n")
        return

    print("\nTicket list\n")
    for ticket in tickets:
        print(f"Flight number: {ticket.get_flight().get_flight_number()}")
        print(f"Airline: {ticket.get_flight().get_airline().get_name()}")
        print(f"Departure: {ticket.get_flight().get_departure_airport().get_name()}")
        print(f"Destination: {ticket.get_flight().get_arrival_airport().get_name()}")
        print(f"Time: {ticket.get_flight().get_time()}")
        print(f"Price: {ticket.get_flight().get_price()}")
        print(f"Seat number: {ticket.get_seat_no()}")
        print(f"Meal type: {ticket.get_meal_type()}")
        print()


def view_airlines(sys: FlightSystem):
    print("\nAirline list\n")
    for airline in sys.get_airlines():
        print(airline.get_name())


def view_airports(sys: FlightSystem):
    print("\nAirport list\n")
    for airport in sys.get_airports():
        print(airport.get_name())
