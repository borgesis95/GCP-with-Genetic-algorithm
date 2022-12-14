from Graph import Graph,Vertex
from Individual import Individual
import random
import numpy as np
from config import POPULATION_SIZE,TOUR_SIZE,SELECTION_MODE,CROSS_PROBABILITY,MUTATION_PROBABILITY,MAX_NUM_VALUTATIONS
class Genetic:
    def __init__(self, graph:Graph):
        self.graph = graph
        self.population = []
        self.stop = False


    def initialize_pop(self):
        vertex = self.graph.vertices
        random.seed()
        count = 0
        while len(self.population) < POPULATION_SIZE:
            colors = [i+1 for i in range(len(vertex))]
            sol = []
            for i in range (len(vertex)):
                color = random.choice(colors)
                sol.append(color)
            if(self.is_valid(sol)):
                self.population.append(Individual(solution=sol))
                count = count + 1

        return self.population
    
                
    def is_valid(self,individual):
         edges = self.graph.edges
     
         return all(self.color(u, individual) != self.color(v, individual)  for u, v in edges)

    def color(self,vertex,individual):
        for index,c in enumerate(individual):
            if vertex == index+1:
                return c

    def run(self):
        instance_t = 0
        fitness_counter = 0

        absolute_best_solution  = Individual(list(range(1,self.graph.number_of_vertex+1)))


        while(not self.stop):
            population_t = []
            instance_t = instance_t + 1

            for _ in range(int(POPULATION_SIZE / 2)):
                    if(SELECTION_MODE =='roulette'):    
                        # --------------------------------------------------------------------------
                        # Roulette Wheel Selection: choose two random parents from the population
                        # with probability proportional to the fitness value of the individuals.
                        # --------------------------------------------------------------------------
                        a,b = random.choices(self.population,[i.fitness for i in self.population], k=2)

                    if(SELECTION_MODE =='tournament'):
                        # --------------------------------------------------------------------------
                        # Tournament Selection: choose two random parents from a tournament of size
                        # K.
                        # --------------------------------------------------------------------------
                        a = min(random.sample(self.population, TOUR_SIZE), key = lambda i :i.fitness)
                        b = min(random.sample(self.population, TOUR_SIZE), key = lambda i: i.fitness)

                    if(SELECTION_MODE =='random'):
                        # --------------------------------------------------------------------------
                        # Random Selection: choose two random parents from the population.
                        # --------------------------------------------------------------------------
                        a, b = random.sample(self.population, 2)

                    # Crossover
                    if(random.random() <= CROSS_PROBABILITY):
                        # ----------------------------------------------------------------------
                        # 1-Point Crossover
                        # ----------------------------------------------------------------------
                        p = random.randint(0, 23)
                        c = Individual(a.solution[0:(p + 1)] + b.solution[(p + 1):])
                        fitness_counter += 1
                        d = Individual(b.solution[0:(p + 1)] + a.solution[(p + 1):])
                        fitness_counter
                    else:
                        c = a
                        d = b

                    # TODO: to implement mutation
                    if (self.is_valid(c.solution)):
                        population_t.append(c)
                  

                    if(self.is_valid(d.solution)):
                        population_t.append(d)
    

            # ------------------------------------------------------------------------------
            # Generational Selection: the offspring population replaces the current
            # population.
            # ------------------------------------------------------------------------------
            self.population = population_t
            mean_fitness = sum([i.fitness for i in self.population]) / POPULATION_SIZE
            std_fitness = np.std([i.fitness for i in self.population])
            best_fitness = min([i.fitness for i in self.population]) 
            
            # print('{0}\t{1}\t{2:.3f}\t{3:.3f}'.format(instance_t, best_fitness, mean_fitness, std_fitness))

            best_solution = sorted(self.population, key = lambda i: i.fitness, reverse=False)[0]
            if best_solution.fitness < absolute_best_solution.fitness:
                absolute_best_solution = best_solution
                evaluations = fitness_counter

            if(fitness_counter > MAX_NUM_VALUTATIONS):
                self.stop = True
             
            print("iteration: ",instance_t, " - The best solution is finded at", evaluations, "is:", absolute_best_solution.solution,"with fitness: ",absolute_best_solution.fitness)
        return absolute_best_solution

                


    