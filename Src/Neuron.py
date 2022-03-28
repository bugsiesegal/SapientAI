from params import NEURON_ENERGY_LOSS_RATE_PROB, NEURON_ENERGY_LOSS_SIGMA
import random


class Neuron:
    """
    Simulates A Neuron.
    """
    def __init__(self, gene_id, neuron_type=0, energy_loss_rate=0, sensory_index=0):
        """
        :param gene_id: Historical Gene Id.
        :param neuron_type: Type of Neuron. 0 is Normal Neuron. 1 is Sensory Neuron. 2 is Action Neuron.
        :param energy_loss_rate: Energy loss rate.
        """

        # Historical Gene Id
        self.gene_id = gene_id

        # Held Energy
        self.energy = 0
        # Rate Energy is lost per step.
        self.energy_loss_rate = 1 - energy_loss_rate

        # Type of Neuron (Normal, Sensory, Action)
        self.neuron_type = neuron_type

        # If sensory which part of input sensory array it looks at.
        self.sensory_index = sensory_index

    def step(self, *args) -> None:
        """
        Loses energy based on energy loss rate. Gains energy based on sensory input.

        :param args: Sensory input.
        """
        self.energy = self.energy_loss_rate * self.energy

        if self.neuron_type == 1:
            self.energy = args[self.sensory_index]

    def to_gene(self) -> list:
        """
        Converts Neuron to gene.

        :return: [Gene id, Energy Loss Rate, Neuron Type, Sensory Index]
        """
        return [self.gene_id, self.energy_loss_rate, self.sensory_index, self.neuron_type]
