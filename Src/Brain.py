from Src.Neuron import Neuron
from Src.Axon import Axon
from Src.params import historical_neuron_genes, historical_axon_genes
import numpy as np


class Brain:
    def __init__(self):
        self.axons = []
        self.neurons = []

    def add_neuron(self, neuron):
        neuron.gene_id = len(historical_neuron_genes)
        historical_neuron_genes.append(len(historical_neuron_genes))
        self.neurons.append(neuron)

    def add_axon(self, axon):
        axon.gene_id = len(historical_axon_genes)
        historical_axon_genes.append(len(historical_axon_genes))
        self.axons.append(axon)

    def step(self, input_array):
        output_array = []

        for neuron in self.neurons:
            output_array.append(neuron.step(*input_array))

        output_array = list(np.asarray(output_array).sum(axis=0))

        for axon in self.axons:
            axon.propagate()

        return output_array

    def to_genome(self) -> tuple[list[list], list[list]]:
        neuron_genome = [neuron.to_gene() for neuron in self.neurons]
        axon_genome = [axon.to_gene() for axon in self.axons]

        return neuron_genome, axon_genome

    @classmethod
    def from_genome(cls, genome: tuple[list[list], list[list]]):
        brain = cls()

        brain.neurons = [Neuron.from_gene(gene) for gene in genome[0]]

        id_to_neuron = {}

        for neuron in brain.neurons:
            id_to_neuron[neuron.gene_id] = neuron

        brain.axons = [Axon.from_gene(gene, id_to_neuron) for gene in genome[1]]

        return brain

