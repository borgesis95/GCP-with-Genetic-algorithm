from Graph import Graph
from Individual import Individual
import random
import numpy as np
from numpy import unique
from Utils import fitness,randomMutation,edgesMutation
from config import MUTATION_TYPE,POPULATION_SIZE,TOUR_SIZE,SELECTION_MODE,CROSS_PROBABILITY,MUTATION_PROBABILITY,REPLACEMENT_PROBABILITY, MAX_NUM_VALUTATIONS,CROSSOVER_TYPE
class Genetic:
    def __init__(self, graph:Graph,colorSize :int):
        self.graph = graph
        self.population = []
        self.stop = False
        self.colorSize = colorSize


    def generatePopulation(self):
        vertex = self.graph.vertices
        random.seed()
        count = 0
        while len(self.population) < POPULATION_SIZE:
            colors = [ i+1 for i in range(self.colorSize)]
            sol = []
            for i in range (len(vertex)):
                color = random.choice(colors)
                sol.append(color)

            ind = Individual(solution=sol)
            ind.fitness  = fitness(self.graph,sol)

            self.population.append(ind)
            count = count + 1
            

        return self.population
    
                
    def isColoringValid(self,individual):
         edges = self.graph.edges
         return all(self.color(u, individual) != self.color(v, individual)  for u, v in edges)

    def color(self,vertex,individual):
        for index,c in enumerate(individual):
            if vertex == index + 1:
                return c

    def run(self,):
        self.generatePopulation()
        instance_t = 0
        fitness_counter = 0
        absolute_best_solution  = Individual()
        absolute_best_solution.fitness = 10000000


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
                            d = Individual(b.solution[0:(p + 1)] + a.solution[(p + 1):])
                            d.fitness = fitness(self.graph,d.solution)
                        
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
                    mean_fitness = sum([i.fitness for i in self.population]) / POPULATION_SIZE
                   
                    if(mean_fitness <=10 and self.colorSize > 4) :
                        # Remove random color --
                        randColToRemove = random.randint(1,self.colorSize-1)
                        randColToReplace = random.randint(1,self.colorSize-1)

                        for i,element in enumerate(c.solution):
                         
                            if(element == randColToRemove):
                                element = randColToReplace
                        
                        for i,element in enumerate(d.solution):
                            if(element == randColToRemove):
                                element = randColToReplace  
                        self.colorSize = self.colorSize -1
                      




                    if (random.random() <=MUTATION_PROBABILITY):
                        c=  edgesMutation(c,VERTEX_NUMBER,self.graph) if MUTATION_TYPE =='edge'  else randomMutation(c,VERTEX_NUMBER)
                      

                    if (random.random() <=MUTATION_PROBABILITY):
                        d=  edgesMutation(d,VERTEX_NUMBER,self.graph) if MUTATION_TYPE =='edge'  else randomMutation(d,VERTEX_NUMBER)
                      

                    c.fitness = fitness(self.graph,c.solution)
                    d.fitness = fitness(self.graph,d.solution)

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
            

            print('counter: {0}\t istanza: {1}\t best_fitness:{2}\t mean fitness: {3}\t deviation :{4}\t'.format(fitness_counter,instance_t, best_fitness, mean_fitness, std_fitness))

            best_solution = sorted(self.population, key = lambda i:  (i.fitness, len(unique(i.solution))),  reverse=False)[0]
        


         
            if best_solution.fitness <= absolute_best_solution.fitness and len(unique(best_solution.solution)) <= len(unique(best_solution.solution)):
                absolute_best_solution = best_solution
                # evaluations = fitness_counter

            if(fitness_counter > MAX_NUM_VALUTATIONS):
                self.stop = True
        

        for i in population_t:
            print("popolazione",i.solution , " -- colori : ",len(unique(i.solution)),'fitness',i.fitness)
       

        print("iteration: ",instance_t, " - The best solution is finded at", "is:", absolute_best_solution.solution,"with fitness: ",absolute_best_solution.fitness,"color: ",len(unique(absolute_best_solution.solution)))
        return absolute_best_solution,True

                


    