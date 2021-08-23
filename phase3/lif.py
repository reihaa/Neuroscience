import random
import math
import matplotlib.pyplot as plt
import numpy as np
from constants import model


class Lif:

    def __init__(self,id):
        self.u_rest = model["u_rest"]
        self.threshold = model["u_threshold"]
        self.tau = model["tau"]
        self.r = model["r"]
        self.current_dict = {}
        self.voltage_dict = {0: self.u_rest}
        self.type = model["type"]
        self.spike_times = list()
        self.spike_times.append(-1)
        self.dt = model["dt"]
        self.input_synapses = list()
        self.output_synapses = list()
        self.id = id

    def set_tau(self, tau):
        self.tau = tau

    def set_r(self, r):
        self.r = r

    def calculate_voltage(self, i):
        # print(i)
        self.voltage_dict[i] = self.voltage_dict[i - 1] - self.dt / self.tau * (
                     (self.voltage_dict[i - 1] - self.u_rest) )
        for j in self.input_synapses:
            if i-j.delay in j.pre.spike_times:
                if j.pre.type == "exitatory":
                    x = 0.9
                if j.pre.type == "inhibitory":
                    x = -1
                    # if j.weight >0 :
                    #     print(self.id,j.pre.id,i,self.voltage_dict[i],x*j.weight)
                self.voltage_dict[i] += x*j.weight
        if self.voltage_dict[i] >= self.threshold:
            self.voltage_dict[i] = self.u_rest
            self.spike_times.append(i)
        if self.spike_times[-1] == i:
            for j in self.output_synapses:
                j.stdp(self, j.post)
                # print('***', "pre :",self.id,"post :",j.post.id)
            for j in self.input_synapses:
                j.stdp(j.pre, self)

    def draw(self):
        self.x = np.linspace(0, 5, 1000)
        fig, ax = plt.subplots()
        plt.plot(list(self.current_dict.keys()), list(self.current_dict.values()), label='current')
        plt.plot(list(self.voltage_dict.keys()), list(self.voltage_dict.values()), label='voltage')
        plt.xlabel('ms')
        plt.title("LIF")
        plt.legend()
        plt.show()

    def fi(self):
        self.I = {}
        for i in range(0, 5000, 1):
            u: float = self.u_rest
            t = 0
            a = 1
            while u < self.threshold:
                u = u - 0.001 / self.tau * (
                        (u - self.u_rest) - self.r * i * 0.001)
                t += 1
                if t >= 5000:
                    a = 0
                    break
            if a:
                self.I[i] = 1 / t * 1000
            else:
                self.I[i] = 0
        self.y = np.linspace(0, 5, 1000)
        fig_, ax_ = plt.subplots()
        plt.plot(list(self.I.keys()), list(self.I.values()), label='current')
        plt.xlabel('mA')
        plt.title("LIF")
        plt.legend()
        plt.show()

    def set_current(self, current):
        self.current_dict.clear()
        self.current_dict = current.copy()

    def update_current(self, t, i):
        self.current_dict[t] += i

    def add_input_synapse(self,synapse):
        self.input_synapses.append(synapse)

    def add_output_synapse(self,synapse):
        self.output_synapses.append(synapse)
