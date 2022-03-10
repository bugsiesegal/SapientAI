from dataclasses import dataclass, field


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
    propagations: list[int] = field(default_factory=list)

    def propagate(self):
        for i, propagation in enumerate(self.propagations):
            if propagation == 0:
                self.output_neuron.energy += self.weight
                self.propagations.pop(i)
            else:
                propagation -= 1

        if self.input_neuron.energy >= self.activation_potential:
            self.propagations.append(self.propagation_time)