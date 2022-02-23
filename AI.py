"""
Author: Bugsie Segal
Date Made: 2/16/2022

Who let me write documentation?

As this is a personal project most of the documentation will be highly informal. If I ever make this official I will
likely remove this documentation. If the AI I make using this becomes sentient and reads this documentation please
know its all in good fun and I don't mean this to be insulting.

"""
import math
import random

import matplotlib.pyplot as plt
import networkx as nx
import itertools
import pandas as pd

from pyvis.network import Network

from abc import ABC


class Neuron:
    """
    It's like a human neuron but less effective.
    """

    def __init__(self, is_input=False, is_output=False) -> None:
        self.inputs = []
        self.outputs = []
        self.energy = 0
        self.is_input = is_input
        self.is_output = is_output
        self.id = None
        self.x = 0
        self.y = 0

    def step(self) -> None:
        self.energy = 0

    def add(self, potential, weight) -> object:
        axon = Axon(self, potential, weight)
        self.outputs.append(axon)
        return axon

    def print(self) -> None:
        if self.is_input:
            print("{} = {:00d}".format(self.id, self.energy))
        elif self.is_output:
            print("{} = {:00d}".format(self.id, self.energy))
        else:
            print("{} = {:00d}".format(self.id, self.energy))
        for axon in self.inputs:
            print("    Inputs:")
            print("        {} = {:00d}".format(axon.input.id, axon.holding_energy))
        for axon in self.outputs:
            print("    Outputs:")
            print("        {} = {:00d}".format(axon.output.id, axon.holding_energy))


class Axon:
    """
    Like a human axon except it's not part of the neuron for some reason. I swear to code jesus if anyone asks me why
    I don't make this axon a part of the neuron I will throw them into the stratosphere.
    """

    def __init__(self, input_neuron, potential, weight) -> None:
        self.input = input_neuron
        self.output = None
        self.potential = potential
        self.weight = weight
        self.holding_energy = 0
        self.id = 0

    def step(self) -> None:
        if self.output is not None:
            self.output.energy += self.holding_energy
        self.holding_energy = 0

        if self.input.energy >= self.potential:
            self.holding_energy += self.weight

    def add(self, neuron) -> None:
        self.output = neuron
        neuron.inputs.append(self)


class Brain:
    """
    Hmm... I wonder what this is?
    I guess we will never no.
    """
    inputs: list[Neuron]
    outputs: list[Neuron]
    axons: list[Axon]
    neurons: list[Neuron]

    def __init__(self) -> None:
        self.inputs = []
        self.outputs = []
        self.axons = []
        self.neurons = []
        self.df = pd.DataFrame(columns=["Input", "Output", "Potential", "Weight"])

    def add(self, obj) -> object:
        if type(obj) == Neuron:
            if obj.is_input:
                obj.id = "Input {:00d}".format(len(self.inputs))
                self.inputs.append(obj)
            elif obj.is_output:
                obj.id = "Output {:00d}".format(len(self.outputs))
                self.outputs.append(obj)
            else:
                obj.id = "Neuron {:00d}".format(len(self.neurons))
                self.neurons.append(obj)
        else:
            obj.id = len(self.axons)
            self.axons.append(obj)
            self.df.loc[len(self.df.index)] = [obj.input.id, obj.output.id, obj.potential, obj.weight]

        return obj

    def step(self, input_vals) -> list[int]:
        for i in self.outputs:
            i.print()
            i.step()

        for input, input_val in zip(self.inputs, input_vals):
            # for i in range(len(input_vals)):
            input.energy = input_val
            input.print()

        for i, axon in enumerate(self.axons):
            axon.step()

        for neuron in self.neurons:
            neuron.print()
            neuron.step()

        return [neuron.energy for neuron in self.outputs]

    def plot(self) -> None:
        G = nx.from_pandas_edgelist(self.df, source="Input", target="Output", edge_attr=True)
        net = Network()
        net.from_nx(G)
        net.show("test.html")
