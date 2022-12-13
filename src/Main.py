from Utils import translate_dimacs_graph
from Genetic import Genetic

pathname='../instances/queen5_5.col'

if __name__ =='__main__':
     graph = translate_dimacs_graph(pathname=pathname)
     ga = Genetic(graph)

     ga.create_population()