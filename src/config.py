
PATHNAME ='./instances/queen5_5.col'
BASE = './instances/'
PATHS = ['DSJC125.9.col','le450_15b.col','le450_15c.col','le450_15d.col']
POPULATION_SIZE = 100
# Tournament size
TOUR_SIZE = 10
# Crossover prob
CROSS_PROBABILITY = 0.9
# Mutation prob
MUTATION_PROBABILITY = 0.1

MEAN_THRESHOLD  = 10
#Replacement U + lambda probability
REPLACEMENT_PROBABILITY = 0.1

MAX_NUM_VALUTATIONS = 10*(10**5)

RUNS = 10
# Value that allow user to select selection's type between : Tournament,Random and Roulette
SELECTION_MODE = 'tournament';

CROSSOVER_TYPE = '1-point'

MUTATION_TYPE ='random'

#--- Graph --
LOGDIR = './logs'