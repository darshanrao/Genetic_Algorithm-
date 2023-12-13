import math
import random



file_name = "input.txt" 
coords = []

initial_route=[]
with open(file_name, "r") as file:
    lines = file.readlines()
    size = int(lines[0].strip())
    for line in lines[1:]:
        x, y, z = map(int, line.split())
        coords.append([x, y, z]) 

#Rule of Thumb : Keeping population size 10 or 20 times the number of nodes
population_size= size*10

     
for i in range(0,size):
    initial_route.append(i)
    
                 
def calculate_distance(node1,node2):
    dist = math.sqrt((node1[0] - node2[0])**2 + (node1[1] - node2[1])**2 + (node1[2] - node2[2])**2)
    return dist

def calculate_total_distance(route,coords):
    sum=0
    n=len(route)
    for i in range(0,n-1):
        sum+=calculate_distance(coords[route[i]],coords[route[i+1]])
    sum+=calculate_distance(coords[route[n-1]],coords[route[0]])
    return sum

# Create  Initial Population 
def CreateInitialPopulation(population_size, cities):
    initial_population= []
    for i in range(0,population_size):
        shuffle_route=cities.copy()
        random.shuffle(shuffle_route)
        initial_population.append(shuffle_route)
        
    return initial_population



initial_population=CreateInitialPopulation(population_size,cities=initial_route)
unique_population= []


## SOLVE THIS 
for population in initial_population:
    if population not in unique_population:
        unique_population.append(population)
        
        
        
def create_RankList(population,coords):     
    # rankList=[]
    # prob=[]
    # sum = 0
    # for route in population:
    #     route_dist=calculate_total_distance(route)
    #     prob.append(1/((route_dist)+1))
    #     sum+= 1/((route_dist)+1)
    
    # for i in range(0,len(prob)):
    #     rankList.append((population[i],prob[i]/sum))
    # rankList = sorted(rankList, key=lambda element: element[1], reverse=True)    
    # return rankList
    
    rank_list = []
    
    for route in population:
        route_distance = calculate_total_distance(route, coords)
        route_fitness = 1 / (route_distance + 1)
        rank_list.append((route, route_fitness))

    rank_list = sorted(rank_list, key=lambda element: element[1], reverse=True)

    return rank_list



rank_list=create_RankList(unique_population)

# print(rank_list)

#Parent Selection and Mating Pool

def roulette_wheel_selection(rank_list):
    index=0
    r=random.random()
    while(r>0):
        r= r-rank_list[index][1]
        index+=1
    index-=1
    
    return rank_list[index][0]


# print(roulette_wheel_selection(rank_list=rank_list))

    
def crossover(parent1,parent2):
    route1= parent1[0]
    route2= parent2[0]
    n = len(parent1[0])
    start=random.randint(0,n-2)
    end=random.randint(start,n-1)
    child1=route1[start:end+1:1]
    child2=route2[start:end+1:1]
    for i in range(0,n):
        if route2[i] not in child1:
            child1.append(route2[i])
        if route1[i] not in child2:
            child2.append(route1[i])
    return child1,child2

# IMPLEMENT MUTATION
# print(crossover(([0, 1, 2, 3], 0.04558532515486248),([2, 1, 3, 0], 0.04736341537782257)))   

def mutation(route, mutation_rate=0.01):
    n = len(route)
    for i in range(n):
        if random.random() < mutation_rate:
            j = random.randint(0, n - 1)
            route[i], route[j] = route[j], route[i]


def create_next_gen(rank_list):
    new_population=[]
    
    for i in range(0,population_size):
        parent1= roulette_wheel_selection(rank_list=rank_list)
        parent2= roulette_wheel_selection(rank_list=rank_list)
        child1,child2=crossover(parent1=parent1,parent2=parent2)
        new_population.append(child1)
        new_population.append(child2)
    
    return new_population
    
# new_p=create_next_gen(rank_list=rank_list)
# rank_list2=create_RankList(new_p)

# print(rank_list)
# print(rank_list2)

new_rank_list=rank_list

count=0
prev_cost=0
it=0
while (True):
    
    new_p=create_next_gen(rank_list=new_rank_list)
    new_rank_list= create_RankList(new_p)
    print('Iteration:',it)
    print('Route:',new_rank_list[0][0])
    cost=round(calculate_total_distance(new_rank_list[0][0]), 3)
    if prev_cost == cost:
        count+=1
    else:
        count=0
    print(count)
    if count > 1000:
        break
    print('Path Cost:',cost )
    prev_cost=cost
    it+=1
    

# print(new_p)