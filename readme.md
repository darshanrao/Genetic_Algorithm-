Genetic Algorithm for Travelling Salesman Problem
This project presents a Genetic Algorithm solution for the Travelling Salesman Problem (TSP), supported by the USC CSCI561 teaching team.

Background
The Travelling Salesman Problem involves finding the shortest possible route that visits a given set of cities/locations exactly once and returns to the starting point. Each location is represented by 3D coordinate points (x, y, z). For instance, (10, 0, 30) represents a city with x=10, y=0, z=30.



How to Run the Algorithm
Clone the Repository:

Install Dependencies:
Ensure you have Python installed. Additionally, the algorithm uses standard libraries, so there's no need for additional installations.

Input File:
Provide the input coordinates in the input.txt file. The format is:

php
Copy code
<number_of_locations>
<x1> <y1> <z1>
<x2> <y2> <z2>
...
Run the Algorithm:
Execute the following command:

bash
Copy code
python tsp_genetic_algorithm.py
Output:
The algorithm will generate an output.txt file containing the best route and its corresponding distance.

Algorithm Overview
Initial Population:
Randomly generates an initial population of routes.

Parent Selection:
Utilizes a Roulette Wheel selection method to choose parents based on their fitness.

Crossover:
Applies a Hybrid Genetic Algorithm (HGA) based crossover method to create offspring.

Mutation:
Introduces random mutations to diversify the population.

Termination:
The algorithm terminates after a specified maximum time or maximum number of generations.

References
CSCI 561- Fall 2023-Homework 1.pdf
Solution of TSP problem based on a hybrid genetic simulated annealing algorithm.pdf

Feel free to explore and modify the algorithm parameters for different TSP instances. If you encounter any issues or have suggestions, please open an issue or pull request.

Happy coding!