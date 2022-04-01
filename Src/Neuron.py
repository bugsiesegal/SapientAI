from Src.params import NEURON_ENERGY_LOSS_RATE_PROB, NEURON_ENERGY_LOSS_SIGMA
import random


class Neuron:
    """
    Simulates A Neuron.
    """
    def __init__(self, neuron_type=0, energy_loss_rate=0, sensory_index=0, action_index=0, output_length=1):
        """
        :param neuron_type: Type of Neuron. 0 is Normal Neuron. 1 is Sensory Neuron. 2 is Action Neuron.
        :param energy_loss_rate: Energy loss rate.
        """

        # Historical Gene Id
        self.gene_id = None

        # Held Energy
        self.energy = 0
        # Rate Energy is lost per step.
        self.energy_loss_rate = energy_loss_rate

        # Type of Neuron (Normal, Sensory, Action)
        self.neuron_type = neuron_type

        # If sensory which part of input sensory array it looks at.
        self.sensory_index = sensory_index

        self.action_index = action_index

        self.output_length = output_length

    def step(self, *args) -> list[float]:
        """
        Loses energy based on energy loss rate. Gains energy based on sensory input.

        :param args: Sensory input.
        """

        out = [0 for i in range(self.output_length)]

        if self.neuron_type == 2:
            out[self.action_index] = self.energy

        self.energy = self.energy_loss_rate * self.energy

        if self.neuron_type == 1:
            self.energy = args[self.sensory_index]

        return out

    def to_gene(self) -> list:
        """
        Converts Neuron to gene.

        :return: [Gene id, Energy Loss Rate, Neuron Type, Sensory Index]
        """
        return [self.gene_id, self.energy_loss_rate, self.sensory_index, self.action_index, self.neuron_type]

    @classmethod
    def from_gene(cls, gene: list) -> "Neuron":
        neuron = cls(gene[4], gene[1], gene[2], gene[3])
        neuron.gene_id = gene[0]
        return neuron
