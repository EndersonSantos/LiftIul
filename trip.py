from datetime import date, datetime, timedelta, time


class Trip:

    def __init__(self, car, departure, adress, type): #car is an instance of Vehicle 
        self.id_car_registration =  str(car.n_trips) + car.car_registration  #adding two properties from vehicle to form the id of the trip
        self.car_registration = car.car_registration
        self.departure = departure
        self.adress = adress
        self.max_ride = int(car.n_available)-1 #The number of seats available minus the driver
        self.passengers = []
        self.type = type
    
    def active(self):    
        """Check if the trip is available based on the time of dparture schedule"""
        go_date_time = self.departure
        text = go_date_time.isoformat()
        go_date_time = datetime.fromisoformat(text)
        myt = datetime.fromisoformat(text)
        now = datetime.now()
        mydt = datetime(now.year, now.month, now.day, myt.hour, myt.minute)
        if (myt.hour - now.hour) >= 0 and (myt.minute - now.minute)>=0:
            return True
        else:
            return False
            
        
    
    def get_datetime(self):
        """Convert the string of time into a date time object"""
        myt = time.fromisoformat(self.departure)
        now = datetime.now()
        mydt = datetime(now.year, now.month, now.day, myt.hour, myt.minute)
        if (mydt-now).days < 0:
            mydt += timedelta(days=1)
        self.departure = mydt
        print(mydt)
    
    def available_rides(self):
        """Allow us to see how much seats are available in an epecific trip"""
        print("Available Seats: ",self.max_ride - len(self.passengers))

    def accept_passengers(self):
        """Check to see if the length of passengers matches the number os seats on the car if so that isn't any seats available"""
        if (self.max_ride - len(self.passengers))>0:
            print("Still have empty seats :)")
        else: 
            print("There isn't any empty seats anymore :( But you can still look for another vehicle :)")
    
    def add_passenger(self, new_passenger):
        """Check to see if theres any available seat an if so add a passenger to the trip"""
        if (self.max_ride - len(self.passengers))>0:
            self.passengers.append(new_passenger)
        else:
            print("There's not empty seats anymore in this trip, Try another one :(")

    def __str__(self):
        return f"Id: {self.id_car_registration},  Car: {self.car_registration}, Departure: {self.departure}, Adress: {self.adress}, Type: {self.type}, Passengers: {[passenger.name for passenger in self.passengers]}"

