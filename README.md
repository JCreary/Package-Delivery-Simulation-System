# Package-Delivery-Simulation-System

Overview

The WGUPS Package Delivery System Simulation is designed to optimize and manage the delivery of packages using multiple trucks. This simulation involves loading packages from a CSV file into a hash table, calculating optimal routes for each truck, and simulating the delivery process. The program also allows for real-time tracking of package status based on user input.

Features

Load Packages: Load package data from a CSV file into a hash table.
Calculate and Load Routes: Calculate optimal routes for trucks and load packages based on package IDs.
Display Loaded Packages: Display the packages loaded onto each truck.
Display All Packages: Display a summary of all loaded packages.
Calculate and Display Routes: Calculate and display the routes and total mileage for each truck.
Simulate Delivery: Simulate the delivery process for all trucks and display delivery logs.
Check Package Status: Check the status of packages by package ID or by a specified time.
File Structure

main.py: Main program file that contains the Main class and the main logic for the simulation.
truck.py: Contains the Truck class that manages truck operations, loading packages, and calculating routes.
hashTable.py: Contains the hashTable class for storing and retrieving package data.
optimization.py: Contains the nextLocation class for optimizing delivery routes.
wgupsPackage.csv: CSV file containing package data.
distanceMatrix.csv: CSV file containing the distance matrix for route calculation.
Classes and Methods

Main Class:

loadPackages(filename): Loads packages from a CSV file into a hash table.
calculateLoadRoutes(truck, package_id, hash_table, distance_matrix): Calculates and loads routes for trucks.
formatRows(row, col_widths): Formats rows for better UI display.
truckPackages(truck): Displays loaded packages for a specific truck.
allPackages(trucks): Displays all loaded packages.
calculateDisplayRoutes(trucks): Calculates and displays truck routes.
simulateDelivery(trucks, distance_matrix): Simulates delivery for all trucks.
packageStatus(trucks): Provides a UI for checking package status.
Running the Program

Ensure you have Python installed on your system.
Place the wgupsPackage.csv and distanceMatrix.csv files in the same directory as the program files.
Run the program using the command: python main.py.
Usage

Upon running the program, you will be presented with a menu of options:

Display packages loaded on Truck 1.
Display packages loaded on Truck 2.
Display packages loaded on Truck 3.
Display all loaded packages.
Calculate and display routes for all trucks.
Simulate delivery for all trucks.
Check package status.
Exit the program.
Example CSV Data

wgupsPackage.csv:

css
Copy code
packageID,hub_names,destination_index,address,city,state,zip,deliveryDeadline,weight,notes,deliveryTime
1,Main Hub,5,123 Elm St,Anytown,UT,84101,10:30 AM,5,,
...
distanceMatrix.csv:

python
Copy code
,Hub,Location 1,Location 2,...
Hub,0,1.2,2.4,...
Location 1,1.2,0,1.5,...
Location 2,2.4,1.5,0,...
...
Notes

Ensure the CSV files are correctly formatted as shown in the example.
The program assumes that the distance matrix and package data are accurate and complete.
The delivery simulation will update package statuses based on the calculated routes and delivery times.
This program provides a comprehensive solution for managing and optimizing package deliveries, making it an ideal tool for logistics and delivery companies. Enjoy using the WGUPS Package Delivery System Simulation!
