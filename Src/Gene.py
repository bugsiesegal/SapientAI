from Src.Axon import Axon
from Src.Neuron import Neuron, Action_Neuron, Sensory_Neuron


class Gene:
    pass


class Neuron_Gene(Gene):
    def __init__(self, energy_loss_rate: float):
        self.energy_loss_rate = energy_loss_rate


class Action_Neuron_Gene(Neuron_Gene):
    pass


class Sensory_Neuron_Gene(Neuron_Gene):
    pass


class Axon_Gene(Gene):
    def __init__(self, input_neuron_id: int, output_neuron_id: int, activation_potential: float, weight: float, propagation_time: int):
        self.propagation_time = propagation_time
        self.weight = weight
        self.activation_potential = activation_potential
        self.output_neuron_id = output_neuron_id
        self.input_neuron_id = input_neuron_id
