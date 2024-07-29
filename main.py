# Author: Jamal Creary



import csv
from truck import Truck
from hashTable import hashTable
from optimization import nextLocation
from datetime import datetime, time

# Creates Main class
class Main:
    # Method loads packages from CSV into a hash table
    @staticmethod
    def loadPackages(filename):
        hash_table = hashTable()
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                package_id = int(row['packageID'])
                hash_table.insert(package_id, row)
        return hash_table

    # Method calculates and load routes for trucks based on the package ID
    @staticmethod
    def calculateLoadRoutes(truck, package_id, hash_table, distance_matrix):
        truck.loadPackages(package_id, hash_table)
        truck.calculationOfOptimalRoute(distance_matrix)

    # Method was created to help format data for a better UI experience
    @staticmethod
    def formatRows(row, col_widths):
        formatted_row = ""
        for i, item in enumerate(row):
            formatted_row += str(item).ljust(col_widths[i] + 2)
        return formatted_row

    # Method displays loaded packages for a specific truck
    @staticmethod
    def truckPackages(truck):
        #Defines column headers
        print(f"\nTruck {truck.truck_id} - Loaded {len(truck.loaded_packages)} packages:")
        headers = ["Package_ID", "Hub_Name", "Destination_Index", "Address", "City", "State", "Zip", "Delivery_Deadline", "Weight", "Notes", "Delivery_Time"]

        col_widths = [len(header) for header in headers]
        # Calculates the maximum column widths based on package details
        for package_id, package in truck.loaded_packages.items():
            row = [
                str(package.packageID),
                package.hub_names,
                str(package.destination_index),
                package.address,
                package.city,
                package.state,
                package.zip,
                package.deliveryDeadline,
                str(package.weight),
                package.notes,
                package.deliveryTime.strftime('%I:%M %p') if package.deliveryTime else 'N/A'
            ]
            col_widths = [max(col_widths[i], len(str(row[i]))) for i in range(len(headers))]

        print(Main.formatRows(headers, col_widths))
        # Print separator line based on total column widths
        print("-" * (sum(col_widths) + 3 * (len(headers) - 1)))

        # Print each package's details in formatted rows
        for package_id, package in truck.loaded_packages.items():
            row = [
                str(package.packageID),
                package.hub_names,
                str(package.destination_index),
                package.address,
                package.city,
                package.state,
                package.zip,
                package.deliveryDeadline,
                str(package.weight),
                package.notes,
                package.deliveryTime.strftime('%I:%M %p') if package.deliveryTime else 'N/A'
            ]
            print(Main.formatRows(row, col_widths))

    # Method displays all loaded packages
    @staticmethod
    def allPackages(trucks):
        print("\n\nSummary of Loaded Packages: ")
        #Defines column headers
        headers = ["Package_ID", "Hub_Name", "Destination_Index", "Address", "City", "State", "Zip", "Delivery_Deadline", "Weight", "Notes", "Delivery_Time"]

        col_widths = [len(header) for header in headers]
        # Calculates the maximum widths based on package details
        for truck in trucks:
            print(f"\nTruck {truck.truck_id} - Loaded {len(truck.loaded_packages)} packages:")
            for package_id, package in truck.loaded_packages.items():
                row = [
                    str(package.packageID),
                    package.hub_names,
                    str(package.destination_index),
                    package.address,
                    package.city,
                    package.state,
                    package.zip,
                    package.deliveryDeadline,
                    str(package.weight),
                    package.notes,
                    package.deliveryTime.strftime('%I:%M %p') if package.deliveryTime else 'N/A'
                ]
                col_widths = [max(col_widths[i], len(str(row[i]))) for i in range(len(headers))]

            print(Main.formatRows(headers, col_widths))
            print("-" * (sum(col_widths) + 3 * (len(headers) - 1)))
            # Print each package's details in formatted rows
            for package_id, package in truck.loaded_packages.items():
                row = [
                    str(package.packageID),
                    package.hub_names,
                    str(package.destination_index),
                    package.address,
                    package.city,
                    package.state,
                    package.zip,
                    package.deliveryDeadline,
                    str(package.weight),
                    package.notes,
                    package.deliveryTime.strftime('%I:%M %p') if package.deliveryTime else 'N/A'
                ]
                print(Main.formatRows(row, col_widths))

    # Method calculates and displays truck routes
    @staticmethod
    def calculateDisplayRoutes(trucks):
        # Total mileage is initialized to 0
        total_mileage = 0.0
        for truck in trucks:
            print(f"\nTruck {truck.truck_id} - Route and Total Mileage:")
            print(f"Route (by destination index): {truck.route}")
            print(f"Total Mileage: {truck.total_mileage:.2f} miles")
            # Creates horizontal bar for table
            print("-" * 40)
            total_mileage += truck.total_mileage
        # Displays total miles traveled by a truck
        print(f"\nTotal Mileage for all trucks: {total_mileage:.2f} miles")

    # Method simulates delivery for all trucks
    @staticmethod
    def simulateDelivery(trucks, distance_matrix):
        for truck in trucks:
            delivery_log = truck.deliveryOfPackages(distance_matrix)
            print(f"\nTruck {truck.truck_id} - Delivery Log:")
            for log_entry in delivery_log:
                #Displays log of delivery
                print(log_entry)
            # Creates horizontal bar for table
            print("-" * 40)

    # Method creates UI/display for package status
    @staticmethod
    def packageStatus(trucks):
        while True:
            # Displays the menu for checking package status
            print("\nSelect one of the given options to check the package status:")
            print("1. By Package ID")
            print("2. Status of packages given a specified time")
            print("3. Go back to main menu")

            # User input
            choice = input("Enter your choice: ")

            if choice == '1':
                while True:
                    # Package ID is requested from user to check package status
                    package_id_input = input("\nEnter the Package ID to check status (Enter 00 to go back to main menu): ")
                    # If user inputs 00 and presses enter, the loop is broken
                    if package_id_input == '00':
                        break  # Exit the inner loop to go back to main menu
                    try:
                        package_id = int(package_id_input)
                        found = False
                        for truck in trucks:
                            package = truck.loaded_packages.get(package_id)
                            if package:
                                # Prints package details, if package ID is found
                                print("\nPackage Details:")
                                print("-" * 256)
                                print(f"Package ID: {package.packageID:<5} | "
                                      f"Truck ID: {truck.truck_id:<5} | "
                                      f"Destination Index: {package.destination_index:<5} | "
                                      f"Address: {package.address:<40} | "
                                      f"City: {package.city:<20} | "
                                      f"Zip: {package.zip:<10} | "
                                      f"Deadline: {package.deliveryDeadline:<10} | "
                                      f"Weight: {package.weight:<5} | "
                                      f"Departure Time: {truck.depart_time.strftime('%I:%M %p') if truck.depart_time else 'Not departed yet':<10} | "
                                      f"Delivery Time: {package.deliveryTime.strftime('%I:%M %p') if package.deliveryTime else 'Not delivered yet':<10}")
                                print("-" * 256)
                                found = True
                        # If the package ID is not found the following error message is displayed
                        if not found:
                            print(f"Package ID {package_id} not found.")
                    # Checks for invalid input
                    except ValueError:
                        print("Use input is invalid. Please enter a valid Package ID or '00' to go back to main menu.")
            elif choice == '2':
                while True:
                    # Allows user to check status based on time
                    time_input = input("\nEnter the time (HH:MM AM/PM - [e.g. 09:00 AM]) to display the delivery status (Enter 00 to go back to main menu): ")
                    try:
                        if time_input.strip().lower() == '00':
                            break  # Exit to package status menu if 00 is entered by the user
                        input_time = datetime.strptime(time_input, '%I:%M %p').time()

                        # Update address for package #9 if current time is after 10:20 AM
                        for truck in trucks:
                            for package_id, package in truck.loaded_packages.items():
                                package.addressUpdate(input_time)

                        # Displays the status of all loaded packages based on user input time
                        print("\nStatus of all loaded packages:")
                        print("-" * 200)
                        print(f"{'Package ID':<10} | {'Truck ID':<10} | {'Destination Index':<15} | {'Address':<40} | {'City':<20} | {'State':<7} | {'Zip':<7} | {'Deadline':<10} | {'Weight':<7} | {'Status':<12} | {'Departure Time':<15} | {'Delivery Time':<15}")
                        print("-" * 200)
                        found_any = False

                        for truck in trucks:
                            for package_id, package in truck.loaded_packages.items():
                                # Delivery time for package
                                delivery_time = package.deliveryTime.time() if package.deliveryTime else time.max
                                # Departure time obtained from truck class
                                departure_time = truck.depart_time.time()

                                # Checks delivery status based on entered time and displays 1 of the 3 status
                                if input_time < departure_time:
                                    status = "At the hub"
                                elif departure_time <= input_time < delivery_time:
                                    status = "En route"
                                else:
                                    status = "Delivered"

                                # Print package status details
                                print(f"{package.packageID:<10} | {truck.truck_id:<10} | {package.destination_index:<17} | {package.address:<40} | {package.city:<20} | {package.state:<7} | {package.zip:<7} | {package.deliveryDeadline:<10} | {package.weight:<7} | "
                                      f"{status:<12} | {truck.depart_time.strftime('%I:%M %p') if truck.depart_time else 'Not departed yet':<15} | {package.deliveryTime.strftime('%I:%M %p') if package.deliveryTime else 'Not delivered yet':<15}")

                                found_any = True
                        # If the package is not found the following error message is displayed
                        if not found_any:
                            print("There are no packages loaded on the trucks.")
                        print("-" * 200)
                    # Checks for invalid input
                    except ValueError:
                        print("User input is invalid. Please enter a valid time (HH:MM AM/PM) or '00' to go back to the main menu.")

            elif choice == 3:
                break
            break # Exits loop

if __name__ == "__main__":
    # Initializes route optimizer and loads the distance matrix
    optimization = nextLocation()
    distance_filename = 'distanceMatrix.csv'
    distance_matrix = optimization.readDistanceMatrix(distance_filename)
    hash_table = Main.loadPackages('wgupsPackage.csv') # Load packages from CSV into hash table

    # Defines the start times for each truck
    start_times = [
        datetime.now().replace(hour=8, minute=0),  # Truck 1 starts at 8:00 AM
        datetime.now().replace(hour=9, minute=6),  # Truck 2 starts at 9:06 AM
        datetime.now().replace(hour=11, minute=33)  # Truck 3 starts at 11:33 AM
    ]

    # Load packages to trucks
    truck_packages = {
        1: [1, 13, 14, 15, 16, 19, 20, 21, 29, 30, 31, 34, 37, 39, 40],
        2: [3, 6, 18, 25, 27, 32, 33, 35, 36, 38],
        3: [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 22, 23, 24, 26, 28]
    }

    # Initialize trucks with speed, starting miles, location based on destination index, start times and packages
    trucks = [
        Truck(truck_id=1, speed=18, miles=0, current_locations=0, depart_time=start_times[0], packages={}),
        Truck(truck_id=2, speed=18, miles=0, current_locations=0, depart_time=start_times[1], packages={}),
        Truck(truck_id=3, speed=18, miles=0, current_locations=0, depart_time=start_times[2], packages={})
    ]

    # Calculates and loads routes for each truck
    for truck in trucks:
        Main.calculateLoadRoutes(truck, truck_packages[truck.truck_id], hash_table, distance_matrix)

    # Prints welcome message
    print("\nWelcome to WGUPS!")

    while True:
        # Displays the main menu options
        print("\nSelect a number to perform an action:")
        print("1. Displays Truck 1 Packages")
        print("2. Displays Truck 2 Packages")
        print("3. Displays Truck 3 Packages")
        print("4. Displays All Packages")
        print("5. Calculates and Displays Routes for All Trucks")
        print("6. Simulates Delivery for All Trucks")
        print("7. Check Package Status (simulate delivery prior to checking status!)")
        print("8. Exit\n")

        # Obtains user input for menu selection
        choice = input("Enter your choice: ")

        if choice == '1':
            Main.truckPackages(trucks[0])
        elif choice == '2':
            Main.truckPackages(trucks[1])
        elif choice == '3':
            Main.truckPackages(trucks[2])
        elif choice == '4':
            Main.allPackages(trucks)
        elif choice == '5':
            Main.calculateDisplayRoutes(trucks)
        elif choice == '6':
            Main.simulateDelivery(trucks, distance_matrix)
            # After simulation, display updated packages for all trucks
            Main.allPackages(trucks)
        elif choice == '7':
            # User must simulate packages prior to checking package status
            Main.packageStatus(trucks)
        elif choice == '8':
            # Exits system
            print("Exiting the system. Goodbye!")
            break
        else:
            # Error check for invalid choice
            print("The user input was invalid. Please enter a value from 1 to 8.")
