from Utils import translate_dimacs_graph
from Genetic import Genetic
import networkx as nx
import matplotlib.pyplot as plt
import random

pathname='./instances/myciel3.col'



def colors(colors_size):
     colors = []

     for i in range(colors_size):
          color = "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])
          colors.append(color)
     return colors 
     
if __name__ =='__main__':
     graph = translate_dimacs_graph(pathname=pathname)
     ga = Genetic(graph)
     pop = ga.initialize_pop()
     bs = ga.run()
     colors = colors(graph.number_of_vertex)
     print("bs.solution",bs.solution)
     print("colors",colors)

     colored_sol = []
     for i,element in enumerate(bs.solution):
          print("node: " ,i+1, "as color:", colors[element-1])
          colored_sol.append(colors[element-1])



     nx.draw(graph.nx,node_color = colored_sol, with_labels = True)
     plt.show()