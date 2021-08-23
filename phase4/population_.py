from lif import Lif


class Population:
    def __init__(self, ex, inh, id):
        self.inhibitory_size = inh
        self.exitatory_size = ex
        self.n = self.inhibitory_size + self.exitatory_size
        self.id = id
        self.initialize_neurons()
        self.pattern = list(range(50))
        self.voltage_mean = list()

    def initialize_neurons(self):
        self.neuron_list = [Lif([self.id, i]) for i in range(self.n)]
        for i in range(self.exitatory_size):
            self.neuron_list[i].type = "exitatory"
        for i in range(self.exitatory_size, self.n):
            self.neuron_list[i].type = "inhibitory"
