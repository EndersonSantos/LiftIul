from user import User
from vehicle import Vehicle
from trip import Trip
import numpy as np
import re

class Manager:

    def __init__(self):
        self.__users = []
        self.__vehicles = []
        self.__trips = []

    
########## User #####################################
    def add_user(self,new_user):
        """Add user in memmory and automatically save in a file"""
        self.__users.append(new_user)
        f = open("user.csv", "a") 
        f.write(f"{new_user}\n")
        f.close()
    
    
    def exits_user(self, new_user_number):
        """Check to see if a user exists in memmory"""
        for user in self.__users:
            if new_user_number not in user.number:
                print("User not in the system") 
                return False
            else: 
                return user

    
    def list_users(self):
        """List all users available in memmory"""
        for user in self.__users:
            print(user)
    
    def change_email(self,user,new_email):
        """Search for a specif user an then call a function from user to allow change the email"""
        for users in self.__users:
            if user == users.number:
                users.change_email(new_email)

    def change_phone(self,user,new_phone):
        """Search for a specif user an then call a function from user to allow change the phone"""
        for users in self.__users:
            if user in users.number:
                users.change_phone(new_phone)

    """
    This function is to load from file into memmory
    def load_file_user(self):
        self.__users=[]
        f = open("user.csv", "r")
        for line in f:
            user_info = (line.strip().split(","))
            c = User(user_info[0], user_info[1], user_info[2], user_info[3],user_info[4])
            self.__users.append(c)            
        f.close()   
    """
    """
    This funtion is to save from memmory into file
    def to_csv_user(self):
        f = open("user.csv", "w")
        for user in self.__users:
            f.write(f"{user}\n")
            print(f"{user}")
        f.close()
    """

########## Vehicle ###########################
    
    def add_vehicle(self,new_vehicle):
        """Add a vehicle into memory and automatically save in a file"""
        self.__vehicles.append(new_vehicle)
        f = open("vehicle.csv", "a")
        f.write(f"{new_vehicle}\n")
        f.close()
    
    def exits_vehicle(self, new_registration):
        """Check to see if the vehicle exists"""
        for vehicle in self.__vehicles:
            if new_registration not in vehicle.car_registration:
                return False
            else:
                 return vehicle

    def change_description(self, car_registration, new_description):
        """Look for a specific vehicle and then allow to change the description of the car"""
        for cars in self.__vehicles:
            if car_registration == cars.car_registration:
                cars.change_description(new_description)

    def list_vehicles(self):
        """List all the vehicles available in memmory"""
        for vehicle in self.__vehicles:
            print(vehicle)
    
    """
    def load_file_vehicle(self):
        self.__vehicle=[]
        f = open("vehicle.csv", "r")
        for line in f:
            vehicle_info = (line.strip().split(","))
            c = Vehicle(vehicle_info[0], vehicle_info[1], vehicle_info[2], vehicle_info[3],vehicle_info[4])
            self.__vehicles.append(c)            
        f.close()   
    """
   
    """
    def to_csv_vehicle(self):
        f = open("vehicle.csv", "w")
        for vehicle in self.__vehicles:   
            f.write(f"{vehicle}\n")
        f.close()
    """

######### Trips #########################################
    def list_trips(self):
        """List all the trips available in memmory"""
        for trips in self.__trips:
            print(trips)
            trips.available_rides()

    def list_trip_adress(self, adress):
        """Allow to search for a trip in a specific area eg: Pinhal Novo"""
        for trips in self.__trips:
            if re.search(adress, trips.adress):
                print(trips)
            else:
                print(f"None trip for {adress} available")
            

    def return_trip(self,id_of_trip):
        """Allow us to grab a specific trip to add a passanger"""
        for trip in self.__trips:
            if id_of_trip in trip.id_car_registration:
                return trip


    def add_trip(self,trip):
        """Allow us to create a enw trip"""
        self.__trips.append(trip)

        
    def add_user_to_trip(self,trip,user):
        """Allow us to add a passenger to a specific trip"""
        return trip.add_passenger(user)


    def save_clean_all(self):
        """Allow us to save all the trips that is alread concluded"""
        f = open("history.csv","a")
        for trip in self.__trips:
            if trip.active():
                pass
            else:
                f.write(f"{trip}\n")
                self.__trips.remove(trip)
        f.close()