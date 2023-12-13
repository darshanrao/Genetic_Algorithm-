import math

# Function to calculate the Euclidean distance between two 3D points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)

# Read the points from the text file
with open('chetan.txt', 'r') as file:
    lines = file.readlines()

points = []
for line in lines:
    x, y, z = map(int, line.strip().split())
    points.append((x, y, z))

# Nearest neighbor algorithm to find the TSP solution
def nearest_neighbor(points):
    n = len(points)
    visited = [False] * n
    path = [0]  # Start from the first point
    total_distance = 0.0

    for _ in range(n - 1):
        current_point = path[-1]
        nearest_point = None
        min_dist = float('inf')

        for i in range(n):
            if not visited[i] and i != current_point:
                dist = distance(points[current_point], points[i])
                if dist < min_dist:
                    min_dist = dist
                    nearest_point = i

        path.append(nearest_point)
        visited[nearest_point] = True
        total_distance += min_dist

    # Return to the starting point to complete the loop
    total_distance += distance(points[path[-1]], points[path[0]])
    path.append(path[0])

    return path, total_distance

# Calculate the TSP solution and total distance
tsp_path, total_distance = nearest_neighbor(points)

# Print the TSP solution and total distance
print("TSP Solution Path (Point Indices):", tsp_path)
print("Total Distance for TSP Solution:", total_distance)
