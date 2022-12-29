from Utils import translate_dimacs_graph,colors,saveGraph,saveRuns
from Genetic import Genetic
from Graph import Graph
import networkx as nx
from config import PATHNAME,RUNS,PATHS,BASE
import matplotlib.pyplot as plt
from numpy import unique
import numpy as np
from humanfriendly import format_timespan
import time

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

def calculation(solutions) :

     colors = []
     mean_colors = 0
     best_color = 0
     sum_colors = 0

     for index,individual in enumerate(solutions):
          len_colors = len(unique(individual.solution))
          sum_colors = sum_colors + len_colors
          colors.append(len_colors)
     
     mean_colors = sum_colors / RUNS
     best_color = min(colors)
     std = np.std([i for i in colors])

     return best_color,mean_colors,std


     

if __name__ =='__main__':

     seeds = [4135, 3359, 2427, 6179, 8757, 6312, 3212, 5432, 6510, 7436]

     for graphPath  in PATHS:
          newPath = BASE + graphPath
          best_sol = []
          graph = translate_dimacs_graph(pathname=newPath)
          start_color_size = getUpperBound(graph)
          ga = Genetic(graph,colorSize=start_color_size)
          path= newPath.split('/')[2] 


          solutions_runs = []
          t_inizial = time.time()

          for run in range(RUNS):
               best_sol = []
               isValid = False
               best_sol,isValid = ga.run(path_name=path,run=run,color_size=start_color_size,seed=seeds[run])
               if(best_sol.solution == None and isValid == False):
                    print("Non è stata trovata nessuna soluzione!")
               else:
                    solutions_runs.append(best_sol)
     
          t_final = time.time()
          total_time = t_final - t_inizial
          time_formatted=format_timespan(total_time)

          best_color,mean,std = calculation(solutions_runs)
          saveRuns(path,best_color,mean,std,time_formatted)
          best_runs = min(solutions_runs, key = lambda i :i.fitness)

          drawGraph(best_runs.solution)

   
    
          
   