from dataclasses import dataclass

import numpy as np

from Src.Neuron import Neuron, Action_Neuron, Sensory_Neuron
from Src.Axon import Axon


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
    def send_sensory_input_to_array(array: np.ndarray[Sensory_Neuron], sensory_input: np.ndarray):
        for i, obj in np.ndenumerate(array):
            obj.sense(sensory_input[i])

    @staticmethod
    def get_action_from_array(array: np.ndarray[Action_Neuron]) -> np.ndarray[float]:
        out_array = np.empty(array.shape)
        for i, obj in np.ndenumerate(array):
            out_array[i] = obj.energy

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
                action.append(action_object)

        return action
