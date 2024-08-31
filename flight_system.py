from datetime import datetime

class Airport:
    def __init__(self, name, country, city):
        self._name = name
        self._country = country
        self._city = city

    def get_country(self):
        return self._country
    
    def get_city(self):
        return self._city
    
    def get_name(self):
        return self._name


class Airline:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


class Flight:
    def __init__(self, flight_no, airline: Airline, departue_airport: Airport, arrival_airport: Airport, time: datetime, price: float):
        self._flight_no = flight_no
        self._airline = airline
        self._date = time.date()
        self._time = time.time()
        self._price = price
        self._departure_airport = departue_airport
        self._arrival_airport = arrival_airport

    def get_flight_number(self):
        return self._flight_no
    
    def get_airline(self):
        return self._airline
    
    def get_time(self):
        return datetime.combine(self._date, self._time)
    
    def get_price(self):
        return self._price
    
    def get_departure_airport(self):
        return self._departure_airport
    
    def get_arrival_airport(self):
        return self._arrival_airport


class Ticket:
    def __init__(self, flight: Flight, seat_no, meal_type):
        self._flight = flight
        self._seat_no = seat_no
        self._meal_type = meal_type


class Customer:
    def __init__(self, name, age, gender, nationality):
        self._name = name
        self._age = age
        self._gender = gender
        self._nationality = nationality
        self._tickets = []

    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def get_gender(self):
        return self._gender
    
    def get_natinality(self):
        return self._nationality
    
    def get_tickets(self):
        return self._tickets
    
    def book_ticket(self, ticket: Ticket):
        self._tickets.append(ticket)


class FlightSystem:
    def __init__(self):
        self.airports = []
        self.airlines = []
        self.flights = dict()
        self.customer = None

    def add_airport(self, airport: Airport):
        self.airports.append(airport)

    def add_airline(self, airline: Airline):
        self.airlines.append(airline)

    def add_flight(self, flight: Flight):
        self.flights[flight.get_flight_number()] = flight

    def login_customer(self, customer: Customer):
        self.customer = customer

    def logout_customer(self):
        self.customer = None
            
    def get_customer(self):
        return self.customer

    def get_airports(self):
        return self.airports

    def get_airport(self, name: str):
        for airport in self.airports:
            if name.capitalize() == airport.get_name().capitalize() or name.capitalize() == airport.get_country().capitalize() or name.capitalize() == airport.get_city().capitalize():
                return airport
            
    def get_airlines(self):
        return self.airlines
    
    def get_airline(self, name: str):
        for airline in self.airlines:
            if name.capitalize() == airline.get_name().capitalize():
                return airline
            
    def get_flight(self, flight_no: int):
        return self.flights[flight_no] if flight_no in self.flights else None
    
    def search_flights(self, search_keys):
        response = []
        for _, flight in self.flights.items():
            is_match = True

            for key, value in search_keys.items():
                if hasattr(flight, "_" + key) and getattr(flight, "_" + key) != value:
                    is_match = False
                    break
                elif not hasattr(flight, "_" + key):
                    raise ValueError(f"Flight has no attribute {key}")

            if is_match:
                response.append(flight)

        return response
