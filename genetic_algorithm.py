import random
import math 
import time
start_time = time.time()
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


def create_RankList(population,coords):     
    rankList=[]
    prob=[]
    sum = 0
    for route in population:
        route_dist=calculate_total_distance(route,coords)
        prob.append(1/((route_dist)+1))
        sum+= 1/((route_dist)+1)
        
    for i in range(0,len(prob)):
        rankList.append((population[i],prob[i]/sum))
    rankList = sorted(rankList, key=lambda element: element[1], reverse=True)    
    return rankList
def roulette_wheel_selection(rank_list):
    index=0
    r=random.random()
    while(r>0):
        r= r-rank_list[index][1]
        index+=1
    index-=1
    
    return rank_list[index][0]

#CHANGE Crossover methods

def crossover(parent1, parent2,coords):
    
    size=len(parent1)
    
    child = [-1] * size
    initial_value=parent1[random.randint(0,len(parent1)-1)]

    arr1=arrRot(parent1,initial_value)
    arr2=arrRot(parent2,initial_value)
    child[0]= parent1[0]
    
    for i in range(size-1):
        dist1 = calculate_distance(coords[arr1[0]],coords[arr1[1]])
        dist2 = calculate_distance(coords[arr2[0]],coords[arr2[1]])
        
        if dist1 < dist2:
            print()
            child[i+1]=arr1[1]
            
        else:
            child[i+1]=arr2[1]
            

        value = child[i+1]
        
        arr1=arrRot(arr1[1:],value)
        arr2=arrRot(arr2[1:],value)  
    child[-1]=arr1[0]   
    
    return child
            
def arrRot(array,value):
    index = array.index(value)
    
    array[:]=array[index:len(array)]+array[0:index]
    
    return array

def mutation(route, mutation_rate=0.05):
    n = len(route)
    for i in range(n):
        if random.random() < mutation_rate:
            j = random.randint(0, n - 1)
            route[i], route[j] = route[j], route[i]
            
            
def genetic_algorithm(coords,max_time,max_generations=20000):
    population_size=120
    initial_route = list(range(len(coords)))
    population = CreateInitialPopulation(population_size, initial_route)
    best_route = None
    best_distance = float('inf')

    for generation in range(max_generations):
        elapsed_time = time.time() - start_time

        rank_list = create_RankList(population, coords)
        current_best=round(calculate_total_distance(rank_list[0][0],coords), 3)
        if current_best < best_distance:
            best_route = rank_list[0][0]
            best_distance = current_best
        if elapsed_time >= max_time:
            output_file(best_route, best_distance,coords)
            break  
        
        new_population = []
        for _ in range(population_size // 2):
            parent1 = roulette_wheel_selection(rank_list)
            parent2 = roulette_wheel_selection(rank_list)
            child1= crossover(parent1, parent2,coords)
            child2= crossover(parent1, parent2,coords)
            mutation(child1)
            mutation(child2)
            new_population.extend([child1, child2])

        population = new_population

    return best_route, best_distance

def output_file(best_route, best_distance,coords):
    f= open("output.txt","w+")
    f.write(str(best_distance)+ "\n")
    for index in best_route:
        x,y,z= coords[index]
        f.write(f"{x} {y} {z}\n") 
    x,y,z= coords[best_route[0]]       
    f.write(f"{x} {y} {z}")
    print(time.time() - start_time)     
    f.close()

def time_limit(size):
    time=0
    if(size>0 and size<=50):
        time=59
    elif(size>51 and size<=100):
        time=74
    elif(size>101 and size<=200):
        time=119
    elif(size>200):
        time=199  
    return time    

if __name__ == "__main__":
    file_name = "input.txt"
    coords = []

    with open(file_name, "r") as file:
        lines = file.readlines()
        size = int(lines[0].strip())
        max_time=time_limit(size)
        for line in lines[1:]:
            x_coord, y_coord, z_coord = map(int, line.split())
            coords.append([x_coord, y_coord, z_coord])

    best_route, best_distance = genetic_algorithm(coords,max_time)
    # output_file(best_route, best_distance,coords)
    print("Best Route:", best_route)
    print("Best Distance:", best_distance)