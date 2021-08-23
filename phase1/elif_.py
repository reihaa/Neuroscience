from lif import Lif
import math
import numpy as np
import matplotlib.pyplot as plt

class Elif(Lif):
    sharpness = 1
    spike_value = 0.7
    u_reset = -0.7

    def set_sharpness(self, sharpness):
        self.sharpness = sharpness

    def cal_u(self):
        self.udic[0] = self.u_rest
        for i in range(1, 5000, 1):
            dv_per_dt = (-(self.udic[i - 1] - self.u_rest) + self.sharpness * np.exp(
                (self.udic[i - 1] - self.u_treshold) / self.sharpness)
                            + self.r * self.idic[i]) / self.tau
            self.udic[i] = self.udic[i - 1] + dv_per_dt * 0.001
            if self.udic[i] >= self.u_treshold:
                self.udic[i-1] = self.spike_value
                self.udic[i] = self.u_reset

    def fi(self):
        self.I = {}
        for i in range(0, 5000, 1):
            u = self.u_rest
            t = 0
            a = 1
            while u < self.u_treshold:
                u = u - 0.001 / self.tau * (
                        (u - self.u_rest) - self.r * i * 0.001 + self.sharpness * np.exp(
                (u - self.u_treshold) / self.sharpness))
                t += 1
                if t >= 50000:
                    a = 0
                    break
            if a:
                self.I[i] = 1 / t *1000
            else:
                self.I[i] = 0
        self.y = np.linspace(0, 5, 1000)
        fig_, ax_ = plt.subplots()
        plt.plot(list(self.I.keys()), list(self.I.values()), label='frecuency')
        plt.xlabel('mA')
        plt.title("elif")
        plt.legend()
        plt.show()