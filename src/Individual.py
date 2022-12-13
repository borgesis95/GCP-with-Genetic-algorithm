from numpy import unique

class Individual:
    def __init__(self, solution = None, nodes = None):
            self.solution = solution
            self.fitness = self.setFitness()

    def setFitness(self):
            self.fitness =  len(unique(self.solution))
            print("solution:",self.solution)
            print("fitness:",self.fitness)


              