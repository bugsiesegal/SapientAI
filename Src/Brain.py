from dataclasses import dataclass

import numpy as np

from Src.Neuron import Neuron, Action_Neuron, Sensory_Neuron
from Src.Axon import Axon
from Src.Gene import NeuronGene, AxonGene, Genome


class Brain:
    def __init__(self):
        self.sensory_neurons = []
        self.action_neurons = []
        self.neurons = []
        self.axons = []

    def add(self, obj):
        if type(obj) == np.ndarray:
            if obj.dtype == Sensory_Neuron:
                self.sensory_neurons.append(obj)
            elif obj.dtype == Action_Neuron:
                self.action_neurons.append(obj)
            else:
                raise ValueError("Requires numpy array of dtype Sensory_Neuron or Action_Neuron")
        elif type(obj) == Sensory_Neuron:
            self.sensory_neurons.append(obj)
        elif type(obj) == Action_Neuron:
            self.action_neurons.append(obj)
        elif type(obj) == Neuron:
            self.neurons.append(obj)
        elif type(obj) == Axon:
            self.axons.append(obj)
        else:
            raise ValueError("Object not supported.")

    @staticmethod
    def send_sensory_input_to_array(array: np.ndarray, sensory_input: np.ndarray):
        for i, obj in np.ndenumerate(array):
            obj.sense(sensory_input[i])

    @staticmethod
    def get_action_from_array(array: np.ndarray) -> np.ndarray:
        out_array = np.empty(array.shape)
        for i, obj in np.ndenumerate(array):
            out_array[i] = obj.energy
            obj.step()

        return out_array

    def step(self, sensory_input):
        for i, sensory_obj in enumerate(self.sensory_neurons):
            if type(sensory_obj) == np.ndarray:
                self.send_sensory_input_to_array(sensory_obj, sensory_input[i])
            else:
                sensory_obj.sense(sensory_input[i])

        for axon in self.axons:
            axon.propagate()

        for neuron in self.neurons:
            neuron.step()

        action = []
        for action_object in self.action_neurons:
            if type(action_object) == np.ndarray:
                action.append(self.get_action_from_array(action_object))
            else:
                action.append(action_object.energy)
                action_object.step()

        return action

    def to_genome(self) -> Genome:
        neuron_genes = []
        axon_genes = []
        neuron_id_dict = {}

        for i, neuron in enumerate(self.neurons + self.action_neurons + self.sensory_neurons):
            if type(neuron) == Neuron:
                neuron_genes.append(NeuronGene(i, neuron.energy_loss_rate, 0))
            elif type(neuron) == Sensory_Neuron:
                neuron_genes.append(NeuronGene(i, neuron.energy_loss_rate, 1))
            else:
                neuron_genes.append(NeuronGene(i, neuron.energy_loss_rate, 2))
            neuron_id_dict[neuron] = i

        for i, axon in enumerate(self.axons):
            axon_genes.append(AxonGene(i, neuron_id_dict[axon.input_neuron], neuron_id_dict[axon.output_neuron],
                                       axon.activation_potential, axon.weight, axon.propagation_time))

        return Genome(neuron_genes, axon_genes)

    @classmethod
    def to_brain(cls, genome: 'Genome'):
        brain = cls()
        id_to_neuron = {}

        for neuron_gene in genome.neuron_genes:
            if neuron_gene.neuron_type == 0:
                new_neuron = Neuron(neuron_gene.energy_loss_rate)
                id_to_neuron[neuron_gene.id] = new_neuron
                brain.add(new_neuron)
            elif neuron_gene.neuron_type == 1:
                new_neuron = Sensory_Neuron(neuron_gene.energy_loss_rate)
                id_to_neuron[neuron_gene.id] = new_neuron
                brain.add(new_neuron)
            else:
                new_neuron = Action_Neuron(neuron_gene.energy_loss_rate)
                id_to_neuron[neuron_gene.id] = new_neuron
                brain.add(new_neuron)

        for axon_gene in genome.axon_genes:
            try:
                new_axon = Axon(id_to_neuron[axon_gene.input_neuron_id], id_to_neuron[axon_gene.output_neuron_id],
                                axon_gene.activation_potential, axon_gene.weight, axon_gene.propagation_time)
                brain.add(new_axon)
            except:
                pass

        return brain
