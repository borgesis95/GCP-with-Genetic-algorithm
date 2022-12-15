from Utils import translate_dimacs_graph,colors
from Genetic import Genetic
from Graph import Graph
import networkx as nx
import matplotlib.pyplot as plt
from config import PATHNAME,COLOR_NUMBER

def getGraphDegree(graph : Graph):
     max_degree = 0
     for vertex in graph.vertices:
          vertex_degree = len(vertex.neighbors)
          if(vertex_degree > max_degree):
               max_degree = vertex_degree     
     return max_degree



if __name__ =='__main__':
     graph = translate_dimacs_graph(pathname=PATHNAME)
     start_color_size = getGraphDegree(graph)
     print("degree:",start_color_size)

     ga = Genetic(graph,colorSize=start_color_size)
     # ga.run()
     # pop = ga.generatePopulation()
     stop = False
     count = 10
     best_sol = []
     lower_bound =  int(start_color_size/4) 
     # lower_bound = 5 

     print("LOWER BOUND",lower_bound)
     while(ga.colorSize >= lower_bound):
          ga.population = []
          bs,isValid = ga.run()

          if(isValid == True):
               best_sol = bs
               if(ga.colorSize >= lower_bound ):
                    ga.colorSize = ga.colorSize-1
          if(isValid == False):
               break
               
     

     print("la soluzione trovata ha un numero di colori pari a ",ga.colorSize)
     colors = colors(graph.number_of_vertex)
     if(best_sol == []):
          print("Non è stata trovata nessuna soluzione!")
     else:
          colored_sol = []
          for i,element in enumerate(best_sol.solution):
               # print("node: " ,i+1, "as color:", colors[element-1])
               colored_sol.append(colors[element-1])
          nx.draw(graph.nx,node_color = colored_sol, with_labels = True)
          plt.show()
   