from numpy import unique
class Individual:
    def __init__(self, solution = None, nodes = None):
            self.solution = solution
            #TODO: to delete
            self.fitness = len(unique(solution))




              