import random
from dataclasses import dataclass

import numpy as np


@dataclass
class Gene:
    id: int


@dataclass
class NeuronGene(Gene):
    """
    Neuron_type: 0 = Normal, 1 = Sensory, 2 = Action
    """
    energy_loss_rate: float
    neuron_type: int


@dataclass
class AxonGene(Gene):
    input_neuron_id: int
    output_neuron_id: int
    activation_potential: float
    weight: float
    propagation_time: int


class Genome:
    def __init__(self, neuron_genes: list[NeuronGene], axon_genes: list[AxonGene]):
        self.neuron_genes = neuron_genes
        self.axon_genes = axon_genes

    def get_connected_axons(self, neuron_id: int) -> list[AxonGene]:
        connected_axons = []

        for axon_gene in self.axon_genes:
            if axon_gene.input_neuron_id == neuron_id or axon_gene.output_neuron_id == neuron_id:
                connected_axons.append(axon_gene)

        return connected_axons

    def get_neuron_by_id(self, neuron_id: int):
        for neuron_gene in self.neuron_genes:
            if neuron_gene.id == neuron_id:
                return neuron_gene

    def get_axon_by_id(self, axon_id: int):
        for axon_gene in self.axon_genes:
            if axon_gene.id == axon_id:
                return axon_gene

    def get_axon_by_connections(self, input_neuron: NeuronGene, output_neuron: NeuronGene):
        for axon_gene in self.axon_genes:
            if axon_gene.input_neuron_id == input_neuron.id and axon_gene.output_neuron_id == output_neuron.id:
                return axon_gene.id
        return None

    def mutate(self, params: dict):
        """
        Mutation_Weights: [Weight Adjustment, New Neuron, New Axon, Remove Neuron, Remove Axon]

        Params: {"Mutation_Weights", "Weight Adj Sigma", "New Axon Act Low", "New Axon Act High", "New Axon Weight Low",
        "New Axon Weight High", "Propagation Time"}
        """
        c = np.random.choice(5, params["Mutation_Weights"])

        if c == 0:
            i = random.randint(0, len(self.axon_genes))

            self.axon_genes[i].weight = random.gauss(self.axon_genes[i].weight, params["Weight Adj Sigma"])
        elif c == 1:
            i = random.randint(0, len(self.axon_genes))

            self.neuron_genes.append(NeuronGene(len(self.neuron_genes), random.random(), 0))

            self.axon_genes.append(AxonGene(len(self.axon_genes),
                                            self.axon_genes[i].input_neuron_id,
                                            len(self.neuron_genes)-1,
                                            random.uniform(params["New Axon Act Low"], params["New Axon Act High"]),
                                            random.uniform(params["New Axon Weight Low"], params["New Axon Weight High"]),
                                            random.randint(0, params["Propagation Time"])
                                            ))

            self.axon_genes.append(AxonGene(len(self.axon_genes),
                                            len(self.neuron_genes) - 1,
                                            self.axon_genes[i].output_neuron_id,
                                            random.uniform(params["New Axon Act Low"], params["New Axon Act High"]),
                                            random.uniform(params["New Axon Weight Low"],
                                                           params["New Axon Weight High"]),
                                            random.randint(0, params["Propagation Time"])
                                            ))
        elif c == 2:
            neuron_connection_points = random.choices(self.neuron_genes, k=2)
            if neuron_connection_points[0].neuron_type != 2 and neuron_connection_points[1].neuron_type != 1 and self.get_axon_by_connections(neuron_connection_points[0], neuron_connection_points[1]) is None:
                self.axon_genes.append(AxonGene(len(self.axon_genes),
                                                neuron_connection_points[0].id,
                                                neuron_connection_points[1].id,
                                                random.uniform(params["New Axon Act Low"], params["New Axon Act High"]),
                                                random.uniform(params["New Axon Weight Low"],
                                                               params["New Axon Weight High"]),
                                                random.randint(0, params["Propagation Time"])
                                                ))

        elif c == 3:
            neuron = random.choice(self.neuron_genes)
            if neuron.neuron_type == 0:
                connected_axons = self.get_connected_axons(neuron.id)
                input_axons = []
                output_axons = []
                for axon in connected_axons:
                    if axon.output_neuron_id == neuron.id:
                        input_axons.append(axon)
                    else:
                        output_axons.append(axon)

                for axon in connected_axons:
                    self.axon_genes.remove(axon)

                self.neuron_genes.remove(neuron)

                for output_axon in output_axons:
                    for input_axon in input_axons:
                        self.axon_genes.append(AxonGene(len(self.axon_genes),
                                                        input_axon.id,
                                                        output_axon.id,
                                                        input_axon.activation_potential+output_axon.activation_potential,
                                                        input_axon.weight+output_axon.weight,
                                                        input_axon.propagation_time+output_axon.propagation_time
                                                        ))

        else:
            self.axon_genes.remove(random.choice(self.axon_genes))
