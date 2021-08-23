from lif import Lif
from synapse import Synapse
from constants import network,model
from current import Current
from population_ import Population
from random import randint
import numpy as np
import matplotlib.pyplot as plt


class Network:
    def __init__(self):
        self.layer_number = network["layer_number"]
        self.layer_size_list = network["layer_size_list"]
        self.populations = list()


    def initialize_populations(self):
        for j in range(len(self.layer_size_list)):
            i = self.layer_size_list[j]
            self.populations.append(Population(i[0],i[1],j))
        return self

    def initialize_synapses(self):
        for i in range(self.layer_size_list[0][0]+self.layer_size_list[0][1]):
            for j in range(self.layer_size_list[1][0]+self.layer_size_list[1][1]):
                synapse = Synapse(self.populations[0].neuron_list[i],self.populations[1].neuron_list[j],np.random.normal(0.1,0.01))
                self.populations[0].neuron_list[i].add_output_synapse(synapse)
                self.populations[1].neuron_list[j].add_input_synapse(synapse)
        synapse = Synapse(self.populations[1].neuron_list[2],self.populations[1].neuron_list[0],np.random.normal(0.1,0.01))
        self.populations[1].neuron_list[2].add_output_synapse(synapse)
        self.populations[1].neuron_list[0].add_input_synapse(synapse)
        synapse = Synapse(self.populations[1].neuron_list[2],self.populations[1].neuron_list[1],np.random.normal(0.1,0.01))
        self.populations[1].neuron_list[2].add_output_synapse(synapse)
        self.populations[1].neuron_list[1].add_input_synapse(synapse)
        #todo
        self.a = list()
        # print("initial weights")
        for i in range(3): #todo
            for j in range(10):
                self.a.append(self.populations[1].neuron_list[i].input_synapses[j].weight)
                # print(j,"->",i," : ",self.populations[1].neuron_list[i].input_synapses[j].weight)
        return self

    def calculate_current(self):
        self.pattern2 = [1,1,0,1,0,1,0,0,1,0]
        self.pattern1 = [1,1,0,0,0,1,0,0,1,0]
        for t in range(1,model["time"],6):
            for i in range(self.layer_size_list[0][0]+self.layer_size_list[0][1]):
                if self.pattern1[i]==1:
                    self.populations[0].neuron_list[i].spike_times.append(t)
            self.calculate_neurons_voltage(t)
            for i in range(self.layer_size_list[0][0]+self.layer_size_list[0][1]):
                if self.pattern1[i] == 2:
                    self.populations[0].neuron_list[i].spike_times.append(t+1)
            self.calculate_neurons_voltage(t+1)
            # print("pattern1 finidhed in time : ",t+1)
            a = randint(0,9)
            self.populations[0].neuron_list[a].spike_times.append(t+2)
            self.calculate_neurons_voltage(t + 2)

            for i in range(self.layer_size_list[0][0] + self.layer_size_list[0][1]):
                if self.pattern2[i]==1:
                    self.populations[0].neuron_list[i].spike_times.append(t + 3)
            self.calculate_neurons_voltage(t+3)
            for i in range(self.layer_size_list[0][0] + self.layer_size_list[0][1]):
                if self.pattern1[i] == 2:
                    self.populations[0].neuron_list[i].spike_times.append(t+4)
            self.calculate_neurons_voltage(t + 4)
            # print("pattern 2 finished in time : ",t+4)
            a = randint(0, 9)
            self.populations[0].neuron_list[a].spike_times.append(t + 5)
            self.calculate_neurons_voltage(t + 5)
            self.b = list()
            # if len(self.populations[1].neuron_list[0].spike_times)>10:
                # print('last spikes of first neuron of second layer :',self.populations[1].neuron_list[0].spike_times[-4::1])
                # print('last spikes of second neuron of second layer :',self.populations[1].neuron_list[1].spike_times[-4::1])
        # print("final weights")
        for i in range(3): #todo
            for j in range(10):
                self.b.append(self.populations[1].neuron_list[i].input_synapses[j].weight)
                #print(j,"->",i," : ",self.populations[1].neuron_list[i].input_synapses[j].weight)
        # for i in range(10):
        #     print(self.populations[0].neuron_list[i].spike_times)
        # print(self.populations[1].neuron_list[0].spike_times)
        print("delay : ",self.populations[1].neuron_list[2].output_synapses[1].delay)
        print("spike times of first neuron: ",len(self.populations[1].neuron_list[0].spike_times))
        print("weight of synapse : ",self.populations[1].neuron_list[2].output_synapses[0].weight)
        print("spike times of second neuron: ",len(self.populations[1].neuron_list[1].spike_times))
        print("weight of synapse : ",self.populations[1].neuron_list[2].output_synapses[1].weight)
        print("spike times of third neuron: ",len(self.populations[1].neuron_list[2].spike_times))
        self.draw()
        return self


    def calculate_neurons_voltage(self,t):
        for i in self.populations:
            for j in i.neuron_list:
                j.calculate_voltage(t)

    def draw(self):
        fig, ax = plt.subplots()
        plt.plot(list(range(30)),self.a, label='inial weight') #todo
        plt.plot(list(range(30)),self.b, label='final weight')
        plt.plot(list(range(10)),self.pattern2,label = 'pattern 2')
        plt.plot(list(range(10,20)),self.pattern1,label="pattern 1")
        plt.title("")
        plt.legend()
        plt.show()
