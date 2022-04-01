import random
from dataclasses import dataclass

from Src.Brain import Brain

from Src.params import NEURON_ENERGY_LOSS_SIGMA, NEURON_ENERGY_LOSS_RATE_PROB, AXON_ENERGY_POTENTIAL_PROB, \
    AXON_ENERGY_POTENTIAL_SIGMA, AXON_WEIGHT_SIGMA, AXON_WEIGHT_PROB


def mutate(genome: tuple[list[list], list[list]]):
    if random.random() < NEURON_ENERGY_LOSS_RATE_PROB:
        i = random.randrange(len(genome[0]))
        genome[0][i][1] = random.gauss(genome[0][i][1], NEURON_ENERGY_LOSS_SIGMA)
    if random.random() < AXON_ENERGY_POTENTIAL_PROB:
        i = random.randrange(len(genome[1]))
        genome[1][i][2] = random.gauss(genome[1][i][2], AXON_ENERGY_POTENTIAL_SIGMA)
    if random.random() < AXON_WEIGHT_PROB:
        i = random.randrange(len(genome[1]))
        genome[1][i][3] = random.gauss(genome[1][i][3], AXON_WEIGHT_SIGMA)
    if random.random() <


class Population:
    def __init__(self, initial_template: Brain, pop_size=10):
        self.genomes = [initial_template.to_genome()] * pop_size

        self.brains = [genome for genome in self.genomes]
