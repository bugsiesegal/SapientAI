import random
from dataclasses import dataclass

from Src.Brain import Brain

from Src.params import NEURON_ENERGY_LOSS_SIGMA, NEURON_ENERGY_LOSS_RATE_MUTATION_PROB, AXON_ENERGY_POTENTIAL_MUTATION_PROB, \
    AXON_ENERGY_POTENTIAL_SIGMA, AXON_WEIGHT_SIGMA, AXON_WEIGHT_MUTATION_PROB, NEW_AXON_MUTATION_PROB

def find_axon_from_connections(input_neuron: list, output_neuron: list, genome: tuple[list[list], list[list]]):
    for axon in genome[1]:
        if axon[1] == input_neuron[0] and axon[2] == output_neuron[0]:
            return axon



def mutate(genome: tuple[list[list], list[list]]):
    if random.random() < NEURON_ENERGY_LOSS_RATE_MUTATION_PROB:
        i = random.randrange(len(genome[0]))
        genome[0][i][1] = random.gauss(genome[0][i][1], NEURON_ENERGY_LOSS_SIGMA)
    if random.random() < AXON_ENERGY_POTENTIAL_MUTATION_PROB:
        i = random.randrange(len(genome[1]))
        genome[1][i][3] = random.gauss(genome[1][i][3], AXON_ENERGY_POTENTIAL_SIGMA)
    if random.random() < AXON_WEIGHT_MUTATION_PROB:
        i = random.randrange(len(genome[1]))
        genome[1][i][4] = random.gauss(genome[1][i][4], AXON_WEIGHT_SIGMA)
    if random.random() < NEW_AXON_MUTATION_PROB:
        a = random.randrange(len(genome[0]))
        b = random.randrange(len(genome[0]))
        if a is not b and


class Population:
    def __init__(self, initial_template: Brain, pop_size=10):
        self.genomes = [initial_template.to_genome()] * pop_size

        self.brains = [genome for genome in self.genomes]
