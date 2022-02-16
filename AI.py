"""
Author: Bugsie Segal
Date Made: 2/16/2022

Who let me write documentation?

As this is a personal project most of the documentation will be highly informal. If I ever make this official I will
likely remove this documentation. If the AI I make using this becomes sentient and reads this documentation please
know its all in good fun and I don't mean this to be insulting.

"""


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

    def step(self) -> None:
        self.energy = 0

    def add(self, potential, weight) -> Axon:
        axon = Axon(self, potential, weight)
        self.outputs.append(axon)
        return axon

    def print(self, i) -> None:
        # Todo: Remove this mess and add in a graphing feature.
        print(self.__hash__())
        print(i)
        for axon in self.inputs:
            axon.input.print(i+1)


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

    def add(self, obj) -> object:
        if type(obj) == Neuron:
            if obj.is_input:
                self.inputs.append(obj)
            elif obj.is_output:
                self.outputs.append(obj)
            else:
                self.neurons.append(obj)
        else:
            self.axons.append(obj)

        return obj

    def step(self, inputs) -> list[int]:
        for i in self.outputs:
            i.step()

        for i in range(len(inputs)):
            self.inputs[i].energy = inputs[i]

        for axon in self.axons:
            print(axon.input.energy)
            axon.step()
            print(axon.output.energy)

        for neuron in self.neurons:
            neuron.step()

        return [neuron.energy for neuron in self.outputs]

    def plot(self) -> None:
        # Todo: Figure out how the hell to plot this mess of a neural structure.
        pass
