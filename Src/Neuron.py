import numpy as np

from Src.Axon import Axon


class Neuron:
    input_axons: list[Axon]
    input_neurons: list['Neuron']
    output_axons: list[Axon]
    output_neurons: list['Neuron']
    energy: float
    energy_loss_rate: float

    def __init__(self, energy_loss_rate: float = 1):
        self.energy_loss_rate = energy_loss_rate
        self.energy_survival_rate = 1 - self.energy_loss_rate
        self.id = None
        self.energy = 0
        self.input_axons = []
        self.input_neurons = []
        self.output_neurons = []
        self.output_axons = []

    def add_input(self, input_axon: Axon):
        self.input_axons.append(input_axon)
        self.input_neurons.append(input_axon.input_neuron)
        Axon.output_neuron = self

    def add_output(self, output_axon: Axon):
        self.output_axons.append(output_axon)
        self.output_neurons.append(output_axon.output_neuron)
        Axon.input_neuron = self

    def step(self):
        self.energy *= self.energy_survival_rate


class Sensory_Neuron(Neuron):
    def add_input(self, input_axon: Axon):
        raise Exception('No input axon for Sensor_Neuron.')

    def sense(self, input_energy):
        self.energy = input_energy

    @staticmethod
    def sensory_array(shape: tuple[int], energy_loss_rate: float = 0):
        a = np.empty(shape, dtype=Sensory_Neuron)
        for i, obj in np.ndenumerate(a):
            a[i] = Sensory_Neuron(energy_loss_rate)

        return a


class Action_Neuron(Neuron):
    def add_output(self, output_axon: Axon):
        raise Exception('No output axon for Action_Neuron.')

    @staticmethod
    def action_array(shape: tuple[int], energy_loss_rate: float = 1):
        a = np.empty(shape, dtype=Action_Neuron)
        for i, obj in np.ndenumerate(a):
            a[i] = Action_Neuron(energy_loss_rate)

        return a
