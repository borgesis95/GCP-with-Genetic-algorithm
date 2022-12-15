from Graph import Graph,Vertex
from Individual import Individual
import random
import numpy as np
from Utils import fitness
from config import POPULATION_SIZE,TOUR_SIZE,SELECTION_MODE,CROSS_PROBABILITY,MUTATION_PROBABILITY,REPLACEMENT_PROBABILITY, MAX_NUM_VALUTATIONS,CROSSOVER_TYPE,COLOR_NUMBER
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
            colors = [ i+1 for i in range(COLOR_NUMBER)]
            sol = []
            for i in range (len(vertex)):
                color = random.choice(colors)
                sol.append(color)

            ind = Individual(solution=sol)
            ind.fitness  = fitness(self.graph,sol)

            self.population.append(ind)
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

        absolute_best_solution  = 0


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
                        a.fitness = fitness(self.graph,a.solution)
                        b.fitness = fitness(self.graph,a.solution)

                    if(SELECTION_MODE =='tournament'):
                        # --------------------------------------------------------------------------
                        # Tournament Selection: choose two random parents from a tournament of size
                        # K.
                        # --------------------------------------------------------------------------
                        a = min(random.sample(self.population, TOUR_SIZE), key = lambda i :i.fitness)
                        b = min(random.sample(self.population, TOUR_SIZE), key = lambda i: i.fitness)
                        a.fitness = fitness(self.graph,a.solution)
                        b.fitness = fitness(self.graph,a.solution)

                    if(SELECTION_MODE =='random'):
                        # --------------------------------------------------------------------------
                        # Random Selection: choose two random parents from the population.
                        # --------------------------------------------------------------------------
                        a, b = random.sample(self.population, 2)
                        
                        a.fitness = fitness(self.graph,a.solution)
                        b.fitness = fitness(self.graph,a.solution)

                    VERTEX_NUMBER = self.graph.number_of_vertex

                    # Crossover
                    if(random.random() <= CROSS_PROBABILITY):
                   
                        if(CROSSOVER_TYPE =='1-point'):
                            # ----------------------------------------------------------------------
                            # 1-Point Crossover
                            # ----------------------------------------------------------------------
                            p = random.randint(0, VERTEX_NUMBER - 2)
                          

                            c = Individual(a.solution[0:(p + 1)] + b.solution[(p + 1):])
                            c.fitness = fitness(self.graph,c.solution)
                            # fitness_counter += 1
                            d = Individual(b.solution[0:(p + 1)] + a.solution[(p + 1):])
                            d.fitness = fitness(self.graph,d.solution)
                            # fitness_counter+=1
                        
                        if(CROSSOVER_TYPE=='2-point'):
                            # 2-Point Crossover
				            # ----------------------------------------------------------------------
                            p1 = random.randint(0, VERTEX_NUMBER - 3)
                            p2 = random.randint(p1 + 1, VERTEX_NUMBER - 2)
                            c = Individual(a.solution[0:(p1 + 1)] + b.solution[(p1 + 1):(p2 + 1)] + a.solution[(p2 + 1):])
                            d = Individual(b.solution[0:(p1 + 1)] + a.solution[(p1 + 1):(p2 + 1)] + b.solution[(p2 + 1):])
                        
                    else:
                        c = a
                        d = b

                    # ------------------------------------------------------------------------------
                    # Mutation
                    # ------------------------------------------------------------------------------

                    if (random.random() <=MUTATION_PROBABILITY):
                        pos = random.randint(0,VERTEX_NUMBER -1)
                        c.solution[pos] = random.randint(1,COLOR_NUMBER)

                    if (random.random() <=MUTATION_PROBABILITY):
                        pos = random.randint(0,VERTEX_NUMBER -1)
                        d.solution[pos] = random.randint(1,COLOR_NUMBER)

                    population_t.append(c)
                    population_t.append(d)
                    fitness_counter+=1
                    
    

            # ------------------------------------------------------------------------------
            # Generational Selection: the offspring population replaces the current
            # population.
            # ------------------------------------------------------------------------------

            if(random.random() <= REPLACEMENT_PROBABILITY):
                self.population = sorted(self.population + population_t, key = lambda i: i.fitness, reverse = True)[0:POPULATION_SIZE]
            else:
                self.population = population_t

            mean_fitness = sum([i.fitness for i in self.population]) / POPULATION_SIZE
            std_fitness = np.std([i.fitness for i in self.population])
            best_fitness = min([i.fitness for i in self.population]) 
            

            print('{0}\t{1}\t{2:.3f}\t{3:.3f}'.format(instance_t, best_fitness, mean_fitness, std_fitness))

            best_solution = sorted(self.population, key = lambda i: i.fitness, reverse=False)[0]
            if(best_solution.fitness == 0) :          
                return best_solution

            if best_solution.fitness < absolute_best_solution:
                absolute_best_solution = best_solution.fitness
                evaluations = fitness_counter

            if(fitness_counter > MAX_NUM_VALUTATIONS):
                print("stop",fitness_counter)
                self.stop = True
             
            # print("iteration: ",instance_t, " - The best solution is finded at", evaluations, "is:", absolute_best_solution.solution,"with fitness: ",absolute_best_solution.fitness)
        return absolute_best_solution

                


    