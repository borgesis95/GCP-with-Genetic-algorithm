from numpy import unique

class Individual:
    def __init__(self, solution = None, nodes = None):
            self.solution = solution
            self.fitness = len(unique(solution))

    # Da capire perchè non funziona
    def setFitness(self):
            self.fitness =  len(unique(self.solution))



              