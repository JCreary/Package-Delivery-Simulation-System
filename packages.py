# Author: Jamal Creary
# Student ID: 000993077
# Title: C950 WGUPS Project
# Submission 1: 07/01/2024

from datetime import time

# Creates truck class
class Package:
    def __init__(self, packageID, hub_names, destination_index, address, city, state, zip, deliveryDeadline, weight, notes, status, departureTime=None, deliveryTime=None):
        # Initialize attributes of the package object
        self.packageID = packageID
        self.hub_names = hub_names
        self.destination_index = destination_index
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryDeadline = deliveryDeadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.departureTime = departureTime
        self.deliveryTime = deliveryTime

    # Method created to update address for package 9
    def addressUpdate(self, input_time):
        # Define corrected time as 10:20 AM
        correct_time = time(10, 20)

        # Check if package ID is 9 and if user input time is before or after corrected time and updates accordingly
        if self.packageID == "9":
            if input_time < correct_time:
                self.address = "300 State St"
                self.zip_code = "84103"
            else:
                self.address = "410 S State St"
                self.zip_code = "84111"
