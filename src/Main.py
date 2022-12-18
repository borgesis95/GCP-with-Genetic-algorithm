from Utils import translate_dimacs_graph,colors,saveGraph
from Genetic import Genetic
from Graph import Graph
import networkx as nx
import matplotlib.pyplot as plt
from config import PATHNAME,RUNS
import matplotlib.pyplot as plt
from numpy import unique


def getUpperBound(graph : Graph):
     max_degree = 0
     for vertex in graph.vertices:
          vertex_degree = len(vertex.neighbors)
          if(vertex_degree > max_degree):
               max_degree = vertex_degree     
     return max_degree


def drawGraph(solution):
     
     colored_sol = []
     colors_created = colors(graph.number_of_vertex)
     for i,element in enumerate(solution):
          colored_sol.append(colors_created[element-1])
     nx.draw(graph.nx,node_color = colored_sol, with_labels = True)
     saveGraph(path,run=run)
     

if __name__ =='__main__':
     best_sol = []
     graph = translate_dimacs_graph(pathname=PATHNAME)
     start_color_size = getUpperBound(graph)
     ga = Genetic(graph,colorSize=start_color_size)
     path= PATHNAME.split('/')[2] 
     
     solutions_runs = []
     for run in range(RUNS):
          best_sol = []
          isValid = False
          best_sol,isValid = ga.run(path_name=path,run=run)
          if(best_sol.solution == None and isValid == False):
               print("Non è stata trovata nessuna soluzione!")
          else:
               solutions_runs.append(best_sol)
     
     best_runs = min(solutions_runs, key = lambda i :i.fitness)

     drawGraph(best_runs.solution)

   
    
          
   