import random
import math
A=[3,7,2,6,4,0,1,5]
B=[5,0,1,2,3,7,4,6]


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

def crossover(parent1, parent2,coords):
    
    size=len(parent1)
    
    child = [-1] * size
    initial_value=parent1[random.randint(0,len(parent1)-1)]

    arr1=arrRot(parent1,initial_value)
    arr2=arrRot(parent2,initial_value)
    child[0]= parent1[0]
    
    for i in range(size-1):
        print(i)
        print(arr1)
        print(arr2)
        print(child)
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
    
    print(child)
            
def arrRot(array,value):
    index = array.index(value)
    
    array[:]=array[index:len(array)]+array[0:index]
    
    return array
    
# crossover(A,B)


if __name__ == "__main__":
    file_name = "input.txt"
    coords = []

    with open(file_name, "r") as file:
        lines = file.readlines()
        size = int(lines[0].strip())
        for line in lines[1:]:
            x_coord, y_coord, z_coord = map(int, line.split())
            coords.append([x_coord, y_coord, z_coord])

    crossover(A,B,coords)