from Utils import translate_dimacs_graph,colors
from Genetic import Genetic
import networkx as nx
import matplotlib.pyplot as plt
from config import PATHNAME




     
if __name__ =='__main__':
     graph = translate_dimacs_graph(pathname=PATHNAME)

     ga = Genetic(graph)
     pop = ga.initialize_pop()
     print("pop",pop[0].solution)
     # bs = ga.run()
     colors = colors(graph.number_of_vertex)


     colored_sol = []
     for i,element in enumerate(pop[0].solution):
          # print("node: " ,i+1, "as color:", colors[element-1])
          colored_sol.append(colors[element-1])



     nx.draw(graph.nx,node_color = colored_sol, with_labels = True)
     plt.show()