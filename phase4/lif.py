import random
import math
import matplotlib.pyplot as plt
import numpy as np
from constants import model, reinforcement


class Lif:

    def __init__(self, id):
        self.da = reinforcement['da']
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
        self.pattern_finishing_times = list()
        self.delay = 1
        self.dopamine_time = list()
        for i in range(model['1/dt'] * model['time']):
            self.dopamine_time.append(0)


    def calculate_voltage(self, i, dopamine):
        if i == 0:
            return dopamine
        self.voltage_dict[i] = self.voltage_dict[i - 1] - self.dt / self.tau * (
            (self.voltage_dict[i - 1] - self.u_rest))
        for j in self.input_synapses:
            if i - j.delay in j.pre.spike_times:
                if j.pre.type == "exitatory":
                    x = 0.1
                if j.pre.type == "inhibitory":
                    x = -0.1
                self.voltage_dict[i] += x * j.weight
        voltage = self.voltage_dict[i]
        if self.voltage_dict[i] >= self.threshold:
            self.voltage_dict[i] = self.u_rest
            self.spike_times.append(i)
            if i + self.delay < len(self.dopamine_time):
                if len(self.pattern_finishing_times) > 0:
                    if i <= self.pattern_finishing_times[-1] + 1:
                        self.dopamine_time[i] = 1
                else:
                    self.dopamine_time[i + self.delay] = -1

        if i < len(self.dopamine_time) and self.dopamine_time[i] != 0:
            dopamine = self.dopamine_handle(self.dopamine_time[i], dopamine)
        for j in self.input_synapses:
            j.synaptic_change(i, dopamine)
        return voltage, dopamine


    def add_input_synapse(self, synapse):
        self.input_synapses.append(synapse)

    def add_output_synapse(self, synapse):
        self.output_synapses.append(synapse)

    def dopamine_handle(self, dopamine_flag, dopamine):
        if dopamine_flag == 1:
            dopamine += self.da
            # print(self.id,1)
        elif dopamine_flag == -1:
            dopamine -= self.da
            # print(self.id,-1)
            if dopamine == 0:
                dopamine -= self.da
        return dopamine
