from Utils import translate_dimacs_graph,colors
from Genetic import Genetic
from Graph import Graph
import networkx as nx
import matplotlib.pyplot as plt
from config import PATHNAME,COLOR_NUMBER
import time
from humanfriendly import format_timespan

def getGraphDegree(graph : Graph):
     max_degree = 0
     for vertex in graph.vertices:
          vertex_degree = len(vertex.neighbors)
          if(vertex_degree > max_degree):
               max_degree = vertex_degree     
     return max_degree



if __name__ =='__main__':
     best_sol = []
     graph = translate_dimacs_graph(pathname=PATHNAME)
     start_color_size = getGraphDegree(graph)

     ga = Genetic(graph,colorSize=start_color_size-5)
     t_inizial = time.time()
     best_sol,isValid = ga.run()
     t_final = time.time()
     total_time = t_final - t_inizial


               
     

     # print("la soluzione trovata ha un numero di colori pari a ",ga.colorSize)
     colors = colors(graph.number_of_vertex)
     print("colori di partenza",start_color_size)
     print('tempo di esecuzione:', format_timespan(total_time))


     if(best_sol == []):
          print("Non è stata trovata nessuna soluzione!")
     else:
          colored_sol = []
          for i,element in enumerate(best_sol.solution):
               colored_sol.append(colors[element-1])
          nx.draw(graph.nx,node_color = colored_sol, with_labels = True)
          plt.show()
   