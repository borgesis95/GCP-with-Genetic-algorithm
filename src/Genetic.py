from Graph import Graph,Vertex
from Individual import Individual
import random
from config import POPULATION_SIZE
class Genetic:
    def __init__(self, graph:Graph):
        self.graph = graph
        self.population = []
        self.stopping_criteria = False


    def create_population(self):
        vertex = self.graph.vertices
        random.seed()
        count = 0
        while len(self.population) < POPULATION_SIZE:
            colors = [i for i in range(len(vertex))]
            sol = []
            for i in range (len(vertex)):
                color = random.choice(colors)
                sol.append(color)
            if(self.is_valid(sol)):
                self.population.append(Individual(solution=sol))
                count = count + 1
    
        print("pop:",self.population.__len__())
                
    def is_valid(self,individual):
         edges = self.graph.edges
         return all(self.color(u, individual) != self.color(v, individual) for u, v in edges)

    def color(self,vertex,individual):
        for index,c in enumerate(individual):
            if vertex == index:
                return c

    def run(self):
        while(not self.stopping_criteria):
            population_t = []
            instance_t = instance_t + 1

            for _ in range(int(POPULATION_SIZE / 2)):
    