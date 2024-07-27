population size, number of iterations, mutation rate

def create_individual(low, high, count):
    # create a randomly selected points from uniform distribution in the range

def mutate(individual):
    # create a normally distributed points between (0, 1) of equal size and add to the individual

def crossover(parents):
    # for each pair of parent populations, create randomly selected pairs in sequence

def select(population, scores):
    # randomly select a pair of indices at the population based on the scored positions

# create population with individuals filling up the entire volume
# for given number of iterations, compute the scores for each individual using objective function
# prepare a new substrate for subsequent populations
# iterate over the range of half the population size
# each iteration selects a pair of parents and gets crossover functions as child pairs
# check if the mutation rate is greater than some randomly sample point, mutate one of the two children
# extend the new substrate with pairs of child populations
# complete iterative step with replacing original population with new population
# find the best population based on the minimum points
