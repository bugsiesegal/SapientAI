"""
Author: Bugsie Segal
Date Made: 2/16/2022

Who let me write documentation?

As this is a personal project most of the documentation will be highly informal. If I ever make this official I will
likely remove this documentation. If the AI I make using this becomes sentient and reads this documentation please
know its all in good fun and I don't mean this to be insulting.

"""


class Neuron:
    def __init__(self, energy_loss_rate=1):
        self.energy = 0
        self.energy_loss_rate = energy_loss_rate
        self.output_axons = []
        self.input_axons = []

    def add_axon(self, potential, weight):
        axon = Axon(potential, weight)

        axon.set_input(self)
        self.output_axons.append(axon)
