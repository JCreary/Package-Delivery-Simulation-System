# Author: Jamal Creary
# Student ID: 000993077
# Title: C950 WGUPS Project
# Submission 1: 07/01/2024

import csv

# Creates route optimization class using nearest neighbor algorithm
class nextLocation:
    def __init__(self):
        pass

    # Function created to read distance from CSV file.
    @staticmethod
    def readDistanceMatrix(filename):
        distance_matrix = []
        with open(filename, mode='r', encoding='utf-8-sig') as file:  # Use 'utf-8-sig' to open CSV file
            reader = csv.reader(file)  # Reads CSV file
            for row in reader:
                distance_matrix.append([float(distance) for distance in row])
        return distance_matrix  # Returns list representing the distance matrix

    # Nearest neighbor function created to find optimal routes
    def nearestNeighborAlgo(self, start_location_index, distance_matrix, delivery_locations):
        # Attribute initialization
        num_locations = len(distance_matrix) # Finds number of locations
        current_location = start_location_index # Starting location
        visited = set([current_location]) # Tracks visited locations
        route = [current_location] # Route including starting location
        total_distance = 0 # Total distance traveled

        # Algorithm continues until all deliveries are completed
        while len(visited) < len(delivery_locations) + 1:
            # Initialize distance and index
            nearest_distance = float('inf')
            nearest_index = None

            # Iterates over delivery locations to find nearest location
            for neighbor in delivery_locations:
                neighbor = int(neighbor)  # Convert neighbor to integer
                if neighbor not in visited:
                    if 0 <= neighbor < num_locations:
                        distance = distance_matrix[current_location][neighbor] #Calculates distance to next location
                        if distance < nearest_distance:
                            nearest_distance = distance
                            nearest_index = neighbor
            # If there are no valid nearest index available, break loop
            if nearest_index is None:
                break

            # Add nearest index to the route and visited routes are noted
            route.append(nearest_index)
            visited.add(nearest_index)
            total_distance += nearest_distance
            current_location = nearest_index

        # If route has more than one location, add distance back to start
        if len(route) > 1:
            total_distance += distance_matrix[route[-1]][route[0]]
            route.append(route[0])

        return route, total_distance # Return calculated route and total distance
