class Vehicle:

    def __init__(self, car_registration, number ,description,n_available,n_trips=0):
        self.__car_registration = car_registration 
        self.__number = number
        self.description = description
        self.n_available = n_available
        self.n_trips = n_trips

    
    @property
    def car_registration(self):
        return self.__car_registration 
    
    @property
    def number(self):
        return self.__number

    def change_description(self, new_description):
        """Allow to change the description of the car"""
        self.description = new_description

    def add_new_trip(self):
        """Allow to add a trip to the car"""
        self.n_trips += 1

    
    def __str__(self):
        return f" Car Registration: {self.car_registration}, Number: {self.__number}, Description: {self.description},Seats Available: {self.n_available}, Number of Trips: {self.n_trips}"


