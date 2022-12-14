from Graph import Graph,Vertex
from Individual import Individual
import random


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
    for u,v in graph.edges:
        if solution[u-1] == solution[v-1]:
            count+=1

    return count

    
