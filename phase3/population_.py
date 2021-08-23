from constants import population as pop
from constants import model
from aelif import Aelif
from current import Current
import random
import numpy as np
import matplotlib.pyplot as plt
from lif import Lif



class Population:
    def __init__(self,ex,inh,id):
        self.inhibitory_size = inh
        self.exitatory_size = ex
        self.j = pop["j"]
        self.mode = pop["mode"]
        self.n = self.inhibitory_size + self.exitatory_size
        self.spike_times_excitatory = list()
        self.spike_times_inhibitory = list()
        self.st = model["time"]
        self.current_plot_x = np.arange(0, self.st)
        self.id = id
        self.initialize_neurons()


    def initialize_neurons(self):
        self.neuron_list = [Lif([self.id,i]) for i in range(self.n)]
        for i in range(self.exitatory_size):
            self.neuron_list[i].type = "exitatory"
        for i in range(self.exitatory_size,self.n):
            self.neuron_list[i].type = "inhibitory"
            print(i,"hh")


    def calculate_current(self):
        for t in range(1, model["time"]):
            ex_spike_time = list()
            in_spike_time = list()
            self.spike_number = 0
            for i in range(self.n):
                postsynaptic_neuron = self.neuron_list[i]
                if postsynaptic_neuron.spike_times[-1] == t-1:
                    self.spike_number += 1
                    if postsynaptic_neuron.type == "exitatory":
                        ex_spike_time.append(i)
                    else:
                        in_spike_time.append(i)
                    cnt = 0
                if postsynaptic_neuron.type == "inhibitory":
                    x = -1
                else:
                    x = 1
                for j in range(self.n):
                    if self.adjacency_matrix[i][j] == 1:
                        postsynaptic_neuron.update_current(t, x * self.weight * self.alpha(j, t - 1))
            self.spike_times_excitatory.append(ex_spike_time)
            self.spike_times_inhibitory.append(in_spike_time)
            for index in range(self.n):
                neuron = self.neuron_list[index]
                neuron.calculate_voltage(t)
            #print(self.spike_number,t)
        return self

    def alpha(self, j, t):  # whether jth neoron has spiked in time t or not
        if t in self.neuron_list[j].spike_times:
            return 1
        else:
            return 0

    def random_mode(self):
        adjacency_matrix = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(int(self.p * self.n)):
                while (True):
                    n = random.randint(0-1, self.n-1)
                    if (n != i and adjacency_matrix[i][n] != 1):
                        break
                adjacency_matrix[i][n] = 1
        return adjacency_matrix

    def full_mode(self):
        adjacency_matrix = [[1 for _ in range(self.n)] for _ in range(self.n)]
        return adjacency_matrix