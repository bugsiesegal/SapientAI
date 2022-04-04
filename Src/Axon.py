from Src.Neuron import Neuron


class Axon:
    """
    Simulates Axon.
    """
    def __init__(self, input_neuron: Neuron, output_neuron: Neuron, activation_potential: float, weight: float):
        self.gene_id = None

        self.input_neuron = input_neuron
        self.output_neuron = output_neuron

        self.activation_potential = activation_potential
        self.weight = weight

    def propagate(self):
        if self.input_neuron.energy >= self.activation_potential:
            self.output_neuron.energy += self.weight

    def to_gene(self):
        return [self.gene_id, self.input_neuron.gene_id, self.output_neuron.gene_id, self.activation_potential, self.weight]

    @classmethod
    def from_gene(cls, gene: list, id_to_neuron: dict[int, Neuron]):
        axon = cls(id_to_neuron[gene[1]], id_to_neuron[gene[2]], gene[3], gene[4])
        axon.gene_id = gene[0]
        return axon
