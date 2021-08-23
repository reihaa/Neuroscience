from synapse import Synapse
from constants import model, reinforcement
from population_ import Population
import numpy as np
import matplotlib.pyplot as plt
import random

dopamine = reinforcement['dopamine']


class Network:
    def __init__(self):
        self.neuron_numbers = 100
        self.input_layer_size = 30
        self.n = 10
        self.inh_size = 20
        self.populations = list()
        self.tau_d = reinforcement["tau_d"]
        self.dopamine_list = list()
        self.dt = model["1/dt"]
        self.p = 0.7
        self.layer_num = int((self.neuron_numbers - self.input_layer_size) / self.n)
        self.output_inh_layer_number = int(self.inh_size / self.layer_num)
        self.output_ex_layer_number = int(self.n - self.output_inh_layer_number)
        self.initialize_populations()
        self.initialize_synapses()
        self.initialize_patterns()

    # initialize populations and store them in list populations, first member is input population
    def initialize_populations(self):
        population = Population(self.input_layer_size, 0, 0)
        self.populations.append(population)
        for i in range(1, self.layer_num + 1):
            population = Population(self.output_ex_layer_number, self.output_inh_layer_number, i)
            self.populations.append(population)

    def initialize_synapses(self):
        for i in self.populations[1::]:
            for j in i.neuron_list:
                a = random.sample(self.populations[0].neuron_list, int(self.populations[0].n * self.p))
                for n in a:
                    synapse = Synapse(n, j, np.random.uniform(0.1, 0.4))
                    n.add_output_synapse(synapse)
                    j.add_input_synapse(synapse)

    def initialize_patterns(self):
        a = list()
        for i in self.populations[1::]:
            b = random.sample(list(range(self.input_layer_size)), 3)
            b.sort()
            while b in a:
                b = random.sample(list(range(self.input_layer_size)), 3)
                b.sort()
            a.append(b)
            pattern = list()
            for j in range(self.input_layer_size):
                if j in b:
                    pattern.append(0)
                else:
                    pattern.append(1)
            i.pattern = pattern

    def time(self, chosen):
        global dopamine
        chosen_pattern = self.populations[chosen].pattern
        for t in range(model['time']):
            for i in range(self.input_layer_size):
                if chosen_pattern[i] == 1:
                    self.populations[0].neuron_list[i].spike_times.append(t*self.dt)
            for n in self.populations[chosen].neuron_list:
                n.pattern_finishing_times.append(t*self.dt)
            self.calculate_neurons_voltage(t)
        return self

    def calculate_neurons_voltage(self, t):
        global dopamine
        for x in range(1, model["1/dt"] + 1):
            for i in self.populations:
                v = 0
                for j in i.neuron_list:
                    voltage, dopamine = j.calculate_voltage(t * model["1/dt"] + x, 0)
                    v += voltage
                v = v / i.n
                i.voltage_mean.append(v)
            delta_d = -dopamine / self.tau_d
            dopamine += delta_d

    def draw(self):
        for i in self.populations[1::]:
            plt.scatter(list(range(model["time"] * model["1/dt"])), i.voltage_mean, s=3, label = i.id)
        plt.legend()
        plt.show()
