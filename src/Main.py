from Utils import translate_dimacs_graph,colors
from Genetic import Genetic
from Graph import Graph
import networkx as nx
import matplotlib.pyplot as plt
from config import PATHNAME


def get_max_degree(graph : Graph):
     max_degree = 0
     for vertex in graph.vertices:
          vertex_degree = len(vertex.neighbors)
          if(vertex_degree > max_degree):
               max_degree = vertex_degree     



if __name__ =='__main__':
     graph = translate_dimacs_graph(pathname=PATHNAME)
     max_degree = get_max_degree(graph)

     ga = Genetic(graph)
     pop = ga.initialize_pop()
     bs = ga.run()
     colors = colors(graph.number_of_vertex)


     colored_sol = []
     for i,element in enumerate(bs.solution):
          # print("node: " ,i+1, "as color:", colors[element-1])
          colored_sol.append(colors[element-1])



     nx.draw(graph.nx,node_color = colored_sol, with_labels = True)
     plt.show()