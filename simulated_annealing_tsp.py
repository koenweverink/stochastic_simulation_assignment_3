
import math
import random

# Function to parse the TSP file and extract city coordinates
def load_tsp_data(filename):
    with open(filename, 'r') as file:
        coords = []
        start_parsing = False
        for line in file:
            line = line.strip()
            if line == "NODE_COORD_SECTION":
                start_parsing = True
                continue
            if line == "EOF" or not line:
                break
            if start_parsing:
                parts = line.split()
                # Ensuring that each line has exactly 3 parts
                if len(parts) == 3 and parts[0].isdigit():
                    _, x, y = parts
                    coords.append((float(x), float(y)))
    return coords



# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Function to calculate the total length of the tour
def total_distance(tour, coords):
    total_dist = 0
    for i in range(len(tour)):
        total_dist += distance(coords[tour[i-1]], coords[tour[i]])
    return total_dist

# Function for the 2-opt Swap
def two_opt_swap(route, i, k):
    new_route = route[:i]
    new_route.extend(reversed(route[i:k + 1]))
    new_route.extend(route[k + 1:])
    return new_route

# Simulated Annealing algorithm
def simulated_annealing(coords):
    # Initial solution (random tour)
    current_tour = list(range(len(coords)))
    random.shuffle(current_tour)
    current_distance = total_distance(current_tour, coords)

    # Parameters
    temp = 10000.0  # Higher initial temperature
    temp_min = 0.001  # Lower minimum temperature
    alpha = 0.995  # Slower cooling rate

    while temp > temp_min:
        i, k = random.sample(range(len(coords)), 2)
        new_tour = two_opt_swap(current_tour, i, k)
        new_distance = total_distance(new_tour, coords)

        # Acceptance probability
        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temp):
            current_tour = new_tour
            current_distance = new_distance

        temp *= alpha

    return current_tour, current_distance

# Main function to run the experiment
def main():
    filename = 'a280.tsp.txt'
    coords = load_tsp_data(filename)
    best_tour, best_distance = simulated_annealing(coords)
    print("Best Tour: ", best_tour)
    print("Best Distance: ", best_distance)

if __name__ == "__main__":
    main()
