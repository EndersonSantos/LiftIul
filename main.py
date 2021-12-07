from manager import Manager
from user import User
from vehicle import Vehicle
from trip import Trip
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

manager = Manager()
#manager.load_file_user()
#manager.load_file_vehicle() 
car = Vehicle("A75462", "456781","BLack-BMW","5")
manager.add_vehicle(car)
user1 = User("55555","Pedro Mota", "Loures;Pirescouxe", "pedro@iscte-iul.pt")
manager.add_user(user1)
trip1 = Trip(car,"13:18","Pinhal Novo","Going")
manager.add_trip(trip1)
car.add_new_trip()
trip1.get_datetime()
trip1.active()

menu = """
1 - List Users
2 - List Vehicles
3 - List Trips
4 - List trips with filter
5 - Register Trip
6 - Passenger Subscription
7 - Register and Remove conclude trips 
8 - System info
9 - Day Activity 
0 - To Finish
"""


input("Press Enter: ")
answer = input("Select a option: ")
while answer!= "0":
   
    if answer == "1":
        print("-"*100)
        manager.list_users()
        print("-"*100)
    
    elif answer == "2":
        print("-"*105)
        manager.list_vehicles()
        print("-"*105)

    elif answer == "3":
        print("-"*123)
        manager.list_trips()
        print("-"*123)

    
    elif answer == "4":
        adress = input("Please select an adress: ")
        print("-"*123)
        manager.list_trip_adress(adress)
        print("-"*123)    



    elif answer == "5":
        car_registration = input("Car Registration: ")
        exists = manager.exits_vehicle(car_registration) 
        if exists!=False: #In this case exists is a vehicle so we just create a new thip for that vehicle
            departure = input("Time of Departure (eg: 19:00, 20:35): ")
            adress = input("Adress: ")
            type = input("Going or Return: ")
            trip = Trip(exists, departure,adress,type)
            try:
               trip.get_datetime()
            except:
                print("select a valid time eg: 19:00, 20:35")
                departure = input("Time of Departure: ") 
                trip = Trip(vehicle, departure,adress,type)
                trip.get_datetime() 
            manager.add_trip(trip)
            exists.add_new_trip()
        else: #In this case exists is false, so we need to register the vehicle using the car registration before creating a trip
            print("Vehicle not register yet in the system")
            number_of_student = input("Number of student: ")
            description_of_the_car = input("Description of the car: ")
            number_of_seats = input("The number of seats available: ")
            vehicle = Vehicle(car_registration, number_of_student,description_of_the_car,number_of_seats)
            print("Car Registered")
            departure = input("Time of Departure: ")
            adress = input("Adress ")
            type = input("Going or Return: ")
            trip = Trip(vehicle, departure,adress,type)
            try:
               trip.get_datetime()
            except:
                print("select a valid time eg: 19:00, 20:35")
                departure = input("Time of Departure: ") 
                trip = Trip(vehicle, departure,adress,type) 
                trip.get_datetime()          
            manager.add_trip(trip)
            vehicle.add_new_trip()

    elif answer == "6":
        user_number = input("User Number: ")
        new_user = manager.exits_user(user_number)
        if new_user!=False: #In this case new_user alread exists so we just add to a trip
            print("User alread in the system")
            trip_to_go = input("What trip would you like to go?(id): ")
            trip_go = manager.return_trip(trip_to_go)
            manager.add_user_to_trip(trip_go,new_user)
        else: #In this case new_user is false so we need first to register the user before adding to a trip
            name = input("Please Enter your Name: ")
            adress_user = input("Please enter your adress: ")
            email = input("Please enter your email: ")
            phone = input("Please enter your phone: ")
            user = User(user_number,name,adress_user,email,phone)
            print("New user created")
            trip_to_go = input("What trip would you like to go?(id): ")
            trip_go = manager.return_trip(trip_to_go)
            manager.add_user_to_trip(trip_go,user)
    
    elif answer == "7":
        manager.save_clean_all() #Clean all the concluded trips that has passed one minute after the departure time
        print("All concluded trips archive")
    

    elif answer == "8":
        choice = input("""
        Select a Option: 
        1 - Users
        2 - Vehicles
        0 - Exit
        """)
        while choice != "0":
            if choice =="1":
                print("-"*105)
                manager.list_users()
                print("-"*105)
                print("""if you want to:
                    1 - Change the email
                    2 - Change the phone
                    0 - Exit
                    """)
                choose = input("Select: ")
                while choose != "0":
                    if choose == "1":
                        id = input("User id: ")
                        new_email = input("New Email: ")
                        manager.change_email(id,new_email)
                    
                    elif choose == "2":
                        id = input("User id: ")
                        new_phone = input("New Phone: ")
                        manager.change_phone(id,new_phone)
                    
                    else:
                        print("invalid Choice please select a valid one")
                    
                    print("""if you want to:
                    1 - Change the email
                    2 - Change the phone
                    0 - Exit
                    """)
                    choose = input("Select: ")    
            elif choice == "2":
                print("-"*105)
                manager.list_vehicles()
                print("-"*105)
                print(""" 
                1 - Change the description
                0 - exit
                """)
                choose = input("Select: ")
                while choose !="0":
                    if choose=="1":
                        car_regist = input("Car Registration: ")
                        new_description = input("New Description: ")
                        manager.change_description(car_regist,new_description)
                    else:
                        print("invalid Choice please select a valid one")
                    
                    print(""" 
                         1 - Change the description
                         0 - exit
                         """)
                    choose = input("Select: ")
            

            else:
                print("invalid Choice please select a valid one")
            
            choice = input("""
            Select a Option: 
            1 - Users
            2 - Vehicles
            0 - Exit
            """)  
    
    
    elif answer == "9":
        mydata = np.zeros([24, 3], int)
        mydata[:,0] = np.arange(24)
        f = open("history.csv","r")
        days = []
        for line in f:
            history_info = (line.strip().split(","))            
            date = history_info[2]
            date = date.split(" ")[2].split("-")[2]
            days.append(int(date))
            time = history_info[2]
            time = time.split(" ")[3].split(":")[0]
            passengers = history_info[5]
            passengers = passengers.split("[")[1].split("]")[0]
            passengers = passengers.split(" ")
            num_of_passengers = len(passengers) 
            mydata[int(time),1]+=1
            mydata[int(time),2]+=int(num_of_passengers)
        f.close() 

        mean_trips_per_day = mydata.sum(axis=0)[1]/len(set(days)) #Set exclude all the repeat numbers so we know how many days were in the list
        mean_per_hour = mydata.sum(axis=0)[2] / 24
        mean_ride_hourly = mydata[:,2].argmax(axis=0) #Grab the max number in the column for count and return the argument
        mean_ride_hourly = mydata[mean_ride_hourly,[0,2]] #Select only the row with the max number and the columns for the hour and the count
        
        print("""
            a - Average Trips per day 
            b - Average Trips per hour 
            c - Time of the day with highest number of rides
            d - Number os trips per hour graphic
            e - Number of rides per hour graphic 
            0 - Exit
            """)
        choose = input("Please select an option: ")
        while choose != "0":
            if choose == "a":
                print("-"*105)
                print(f"Average Trips per day: {np.round(mean_trips_per_day,3)}")
                print("-"*105)
            elif choose =="b":
                print("-"*105)
                print(f"Average Trips per Hour: {np.round(mean_per_hour,3)}")
                print("-"*105)
            elif choose =="c":
                print("-"*105)
                print(f"Max num of ride: hour-{np.round(mean_ride_hourly[0],3)} num-{mean_ride_hourly[1]}")
                print("-"*105)
            elif choose =="d":
                sns.barplot(x=mydata[:,0],y=mydata[:,1])        
                plt.title("Number of trips per each hour")
                plt.xlabel("Hours of the day")
                plt.ylabel("Number of Trips")
                plt.show()
            elif choose =="e":
                sns.barplot(x=mydata[:,0],y=mydata[:,2])
                plt.title("Number of rides per each hour")
                plt.xlabel("Hours of the day")
                plt.ylabel("Number of rides")
                plt.show()
    
            else:
                print("invalid Choice please select a valid one")
            
            print("""
            a - Average Trips per day 
            b - Average Trips per hour 
            c - Time of the day with highest number of rides
            d - Number os trips per hour graphic
            e - Number of rides per hour graphic 
            0 - Exit
            """)
            choose = input("Please select an option: ")
    
    else:
        print("Invalid input select a valid one")


    print(menu)
    answer = input("Select a option: ")
    





     