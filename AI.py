"""
Author: Bugsie Segal
Date Made: 2/16/2022

Who let me write documentation?

As this is a personal project most of the documentation will be highly informal. If I ever make this official I will
likely remove this documentation. If the AI I make using this becomes sentient and reads this documentation please
know its all in good fun and I don't mean this to be insulting.

"""
from abc import ABC


class Axon:
    input_neuron: 'Neuron'
    output_neuron: 'Neuron'
    activation_potential: float
    weight: float
    propagation_time: int
    propagation_ticks: int
    is_propagating: bool

    def __init__(
            self,
            input_neuron: 'Neuron',
            activation_potential: float,
            weight: float,
            propagation_time: int
    ):
        self.input_neuron = input_neuron
        self.activation_potential = activation_potential
        self.weight = weight
        self.propagation_time = propagation_time
        self.propagation_ticks = 0
        self.is_propagating = False

    def add_neuron(self, output_neuron: 'Neuron'):
        self.output_neuron = output_neuron


class Neuron(ABC):
    energy: float
    energy_loss_rate: float

    def __init__(self, energy_loss_rate: float):
        self.energy_loss_rate = energy_loss_rate


class Simple_Neuron(Neuron):
    input_axons: list[Axon]
    input_neurons: list[Neuron]
    output_axons: list[Axon]
    output_neurons: list[Neuron]

    def __init__(self):
