from Graph import Graph,Vertex
from Individual import Individual
import random
from numpy import unique
import os  
import matplotlib.pyplot as plt


# This method allow to convert dimacs standard on Graph class 
def translate_dimacs_graph(pathname):
    graph = Graph()
    with open(pathname,mode='r') as file:
        #Read each line and take just line which start with 'e' that means edge according to dimacs standard
        for line in file.readlines():
            if line.split()[0] =='p':
                number_of_vertex  = int(line.split()[2])
                number_of_edges = int(line.split()[3])
                graph.number_of_vertex =number_of_vertex
                graph.number_of_edges = number_of_edges

                # Vertex creation
                for index in range(number_of_vertex):
                     graph.vertices.append(Vertex(index+1))
                     graph.nx.add_node(str(index+1))
                  
            if line.split()[0] =='e':
                u = int(line.split()[1])
                v = int(line.split()[2])

                graph.edges.append((u,v))
                graph.nx.add_edge(str(u),str(v))
                
                graph.vertices[u-1].neighbors.append(v)

    return graph        


def colors(colors_size):
     colors = []
     for i in range(colors_size):
          color = "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])
          colors.append(color)
     return colors 


def fitness(graph:Graph,solution):
    count = 0
    solutionsColor = len(unique(solution))
    for u,v in graph.edges:
        if solution[u-1] == solution[v-1]:
            count+=1

    return (count * solutionsColor) + solutionsColor



def randomMutation(ind : Individual,vertexNumber : int):
      pos = random.randint(0,vertexNumber -1)
      colors = len(unique(ind.solution))
      ind.solution[pos] = random.randint(1,colors)
      return ind


def edgesMutation(ind  : Individual,vertexNumber : int,graph: Graph):
    pos = None
    colors = len(unique(ind.solution))
    for u,v in graph.edges:
        if(ind.solution[u-1] == ind.solution[v-1]):
            pos = v-1
            break
    if(pos != None):
        ind.solution[pos] =  random.randint(1,colors) 
    return ind

def newEdgeMutation(sol : Individual, graph: Graph):

    solution = sol
    colors = len(sol.solution)
    vertices = len(sol.solution) 
    coloriUti = len(unique(sol.solution))
    colorsChanged  = 0
    for vertex in range(vertices):
        neighbors = graph.vertices[vertex].getNeighbors()
        for neighbor in neighbors:
            if(sol.solution[vertex] == sol.solution[neighbor-1]):
                color = random.randint(1,colors)
                sol.solution[vertex] = color 
                # sol.solution[neighbor-1] = colo r
                colorsChanged = colorsChanged + 1

    if(colorsChanged == 0):
        position = random.randint(0,len(sol.solution)-1)
        randomPosition = random.randint(0,len(sol.solution)-1)
        newColor = sol.solution[randomPosition]
        if(sol.solution[position] == sol.solution[randomPosition]):
            sol.solution[position] = random.randint(1,colors)
        else :
            sol.solution[position] = newColor


    # print("fitness",fitness(graph,sol.solution) - coloriUti )
    # print("positionChanged",colorsChanged)
    # print("solution",solution.solution)
    return solution
    

def save(istance_name:str,run : int,data):
    path = 'results_test_2/' + istance_name+'/'+ 'run('+ str(run)+')/'
    if not os.path.exists(path):
        os.makedirs(path)
    pathfile = path + istance_name + '.txt'

    file = open(pathfile,'a')
    file.writelines(data)

def saveRuns(istance_name:str, bc:int, mean:float,std:float,time :str):
    path = 'results_test_2/' + istance_name 
    value   ='istance: '+ istance_name +  '  bc: ' + str(bc) +'  mean: ' + str(mean) +'  std: '+ str(std) + '  stime: ' + time
    if not os.path.exists(path):
        os.makedirs(path)
    pathfile = path  + '.txt'
    print("pathfile",pathfile)
    file = open(pathfile,'a')
    file.writelines(value)

def saveGraph(istance_name:str,run:int):
    path = 'results_test_2/' + istance_name
    if not os.path.exists(path):
            os.makedirs(path)
    pathfile = path  + '.png'
    plt.savefig(pathfile)




    
