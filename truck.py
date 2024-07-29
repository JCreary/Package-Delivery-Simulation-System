# Author: Jamal Creary
# Student ID: 000993077
# Title: C950 WGUPS Project
# Submission 1: 07/01/2024


from datetime import timedelta
from packages import Package
from optimization import nextLocation

# Creates truck class
class Truck:
    def __init__(self, truck_id, speed, miles, current_locations, depart_time, packages):
        # Initialize attributes of the Truck object
        self.truck_id = truck_id
        self.speed = speed
        self.miles = miles
        self.current_locations = current_locations
        self.depart_time = depart_time
        self.packages = packages
        self.loaded_packages = {}
        self.route = []
        self.total_mileage = 0.0

    # Load packages function loads packages onto trucks using the package ID
    def loadPackages(self, package_ids, hash_table):
        for package_id in package_ids:
            package_data = hash_table.search(package_id) # Searches for package in the hash table
            if package_data:
                # Creates package object
                package = Package(
                    package_data['packageID'],
                    package_data['hub_names'],
                    package_data['destination_index'],
                    package_data['address'],
                    package_data['city'],
                    package_data['state'],
                    package_data['zip'],
                    package_data['deliveryDeadline'],
                    package_data['weight'],
                    package_data['notes'],
                    status=None,
                    departureTime=None,
                    deliveryTime=None
                )
                self.loaded_packages[package_id] = package
            else:
                print(f"Package {package_id} not found in hash table") #  If package ID is not found, error message is displayed

    # Function calculates the optimal delivery routes using the nearest neighbor algorithm
    def calculationOfOptimalRoute(self, distance_matrix):
        if not self.loaded_packages:
            print(f"No packages loaded on Truck {self.truck_id}. Cannot calculate route.") # Error message displayed if no packages are loaded
            self.route = [self.current_locations] + self.route  # Add initial location to route
            print(f"Truck {self.truck_id} route calculated: {self.route}")
            return

        # Extract locations from loaded packages
        delivery_locations = [package.destination_index for package in self.loaded_packages.values()]

        # Initialize nextLocation
        optimization = nextLocation()

        # Calculates the route using nearest neighbor algo starting from hub (location 0)
        route, total_distance = optimization.nearestNeighborAlgo(0, distance_matrix, delivery_locations)

        self.route = route  # Set the calculated route
        self.total_mileage = total_distance  # Calculate total mileage based on the route


    # Simulates the delivery of packages based on the calculated route and updates the delivery log
    def deliveryOfPackages(self, distance_matrix):
        delivery_log = []
        current_depart_time = self.depart_time # Starts from trucks departure times
        current_locations = 0

        for next_location in self.route[1:]:  #Iterates through each location in route
            delivered_packages = []
            for package_id, package in self.loaded_packages.items():
                if int(package.destination_index) == next_location and package_id not in delivered_packages:
                   # Calculates travel time to next location
                    travel_time_hours = distance_matrix[current_locations][next_location] / self.speed
                   # Calculates delivery time
                    delivery_time = current_depart_time + timedelta(hours=travel_time_hours)
                    package.deliveryTime = delivery_time
                    current_depart_time = delivery_time
                    current_locations = next_location

                    # Log the delivery
                    delivery_log.append(
                        f"Delivered package {package.packageID} to {package.address}, {package.city} at {delivery_time.strftime('%I:%M %p')}"
                    )
                    delivered_packages.append(package_id)  # Packages are added and classified as delivered
        # Returns delivery log
        return delivery_log
