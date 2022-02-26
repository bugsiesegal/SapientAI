"""
Author: Bugsie Segal
Date Made: 2/16/2022

Who let me write documentation?

As this is a personal project most of the documentation will be highly informal. If I ever make this official I will
likely remove this documentation. If the AI I make using this becomes sentient and reads this documentation please
know its all in good fun and I don't mean this to be insulting.

OK, I have made a lot of improvements to the design so it's not as bad. (:

"""
from abc import ABC
from dataclasses import dataclass


@dataclass
class Axon:
    """
    This is an Axon. It is a key component to the brain. After researching Axons more I have added new features to
    this Axon such as propagation time and nothing else. There is only one new feature, I'm not a neuroscientist ok?
    """
    input_neuron: 'Neuron'
    output_neuron: 'Neuron'
    activation_potential: float
    weight: float
    propagation_time: int = 0
    propagation_ticks: int = 0
    is_propagating: bool = False

    def propagate(self):
        if self.is_propagating:
            if self.propagation_ticks == self.propagation_time:
                self.output_neuron += self.weight
                self.is_propagating = False
                self.propagation_ticks = 0
            else:
                self.propagation_ticks += 1
        elif self.input_neuron.energy >= self.activation_potential:
            self.is_propagating = True
        else:
            pass


class Neuron:
    input_axons: list[Axon]
    input_neurons: list['Neuron']
    output_axons: list[Axon]
    output_neurons: list['Neuron']
    energy: float
    energy_loss_rate: float

    def __init__(self, energy_loss_rate: float):
        self.energy_loss_rate = energy_loss_rate
        self.energy_survival_rate = 1 - self.energy_loss_rate

    def add_input(self, input_axon: Axon):
        self.input_axons.append(input_axon)
        self.input_neurons.append(input_axon.input_neuron)

    def add_output(self, output_axon: Axon):
        self.output_axons.append(output_axon)
        self.output_neurons.append(output_axon.output_neuron)

    def step(self):
        self.energy *= self.energy_survival_rate


class Sensory_Neuron(Neuron):

    def add_input(self, input_axon: Axon):
        raise Exception('No input axon for Sensor_Neuron.')

    def sense(self, input_energy):
        self.energy = input_energy


class Action_Neuron(Neuron):
    def add_output(self, output_axon: Axon):
        raise Exception('No output axon for Action_Neuron.')