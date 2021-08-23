from lif import Lif
from synapse import Synapse
from constants import network
from population_ import Population
from current import Current
import matplotlib.pyplot as plt
import numpy as np

class Network:
    def __init__(self):
        #self.layer_number = network["layer_number"]
        #self.layer_size_list = network["layer_size_list"]
        #self.populations = list()
        self.STDP()
        self.draw()

    def STDP(self):
        #for i in range(self.layer_number):
         #   self.populations.append(Population(self.layer_size_list[i]))
        self.neuron1 = Lif()
        self.neuron2 = Lif()
        self.neuron1.spike_times = [1]
        self.neuron2.spike_times = [2]
        for i in range (2,40,2):
            self.neuron1.spike_times.append(self.neuron1.spike_times[-1]+i)
            self.neuron2.spike_times.append(self.neuron2.spike_times[-1]+i+1)
        self.synapse = Synapse(self.neuron1,self.neuron2)
        for i in range(len(self.neuron2.spike_times)-1):
            self.synapse.stdp(self.neuron1.spike_times[i],self.neuron2.spike_times[i])
            self.synapse.stdp(self.neuron1.spike_times[i+1],self.neuron2.spike_times[i])
        print(list(self.synapse.time), list(self.synapse.delta_w_list))

    def draw(self):
        self.x = np.linspace(0, 5, 1000)
        fig, ax = plt.subplots()
        plt.scatter(list(self.synapse.time), list(self.synapse.delta_w_list))
        plt.xlabel('time')
        plt.ylabel('delta w')
        plt.title("STDP")
        #plt.legend()
        plt.show()
