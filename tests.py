from vehicle import Vehicle
from trip import Trip
from datetime import datetime, time
"""
car = Vehicle("A75462", "456781","BLack-BMW",5)
trip1 = Trip(car, "19:00","Pinhal Novo")
trip1.get_datetime()
print(trip1.departure)
trip1.active()
"""


"""      
user1 = User("55555","Pedro Mota", "Loures;Pirescouxe", "pedro@iscte-iul.pt")
user2 = User("66666","Maria Mercedes", "Sintra;Rio de Mouro", "maria@iscte-iul.pt", "966666666") 
manager.add_user(user1)
manager.add_user(user2)
new_user = User("456789","Enderson Santos", "Setubal;Pinhal Nono","a@gmail.com","948563217")
print(manager.exits_user(new_user))
manager.add_user(new_user)
manager.list_users()
manager.to_csv_user()
"""

"""
car1 = Vehicle("A75462", "456781","BLack-BMW",5)
car2 = Vehicle("A67842","684212", "Black - Mercedes",5)
manager.add_vehicle(car1)
manager.add_vehicle(car2)
new_car = Vehicle("A675235", "698451","Yelow-Camaro",4)
print(manager.exits_vehicle(new_car))
manager.list_vehicles()
manager.to_csv_vehicle()
"""

"""
print(menu)
car = Vehicle("A75462", "456781","BLack-BMW",5)
manager.add_vehicle(car)
trip1 = Trip(car, "19:00","Pinhal Novo","Going")
user1 = User("55555","Pedro Mota", "Loures;Pirescouxe", "pedro@iscte-iul.pt")
manager.add_user(user1)
manager.add_user_to_trip(trip1,user1)
manager.add_trip(trip1)
car.add_new_trip()
trip2 = Trip(car, "19:00","Pinhal Novo","Going")
user1 = User("55555","Pedro Mota", "Loures;Pirescouxe", "pedro@iscte-iul.pt")
user2 = User("66666","Maria Mercedes", "Sintra;Rio de Mouro", "maria@iscte-iul.pt", "966666666")
manager.add_user_to_trip(trip2,user1)
manager.add_user_to_trip(trip2,user2)
manager.add_trip(trip2)"""

"""
test = ["Id: 0A75462,  Car: A75462, Departure: 2021-12-05 17:14:00, Adress: Pinhal Novo, Type: Going, Passengers: [Enderson Carla Joao]",\
    "Id: 0A75462,  Car: A75462, Departure: 2021-12-06 13:18:00, Adress: Pinhal Novo, Type: Going, Passengers: [Pedro]"]

for line in test:
    history_info = (test.strip().split(","))            
    date = history_info[2]
    date = date.split(" ")[2].split("-")[2]
    days = [int(date)]
print(set(days))
time1 = history_info[2]
time1 = time1.split(" ")[3].split(":")[0]
passengers = history_info[5]
passengers = passengers.split("[")[1].split("]")[0] 
passengers = passengers.split(" ")
num_of_passengers = len(passengers) 
"""