import random
import math
import matplotlib.pyplot as plt
import numpy as np
from lif import Lif
from elif_ import Elif


class Aelif(Elif):
    tau_w = 3
    w = {}
    w[0] = 0
    a = 3
    b = 0.5
    spike_times = list()

    def cal_u(self):
        self.spike_times.append(0)
        self.udic[0] = self.u_rest
        for i in range(1, 5000):
            self.cal_w(i)
            dv_per_dt = (-(self.udic[i - 1] - self.u_rest) + self.sharpness * np.exp(
                (self.udic[i - 1] - self.u_treshold) / self.sharpness) - 3 * self.r * self.w[
                             i] + self.r * self.idic[i]) / self.tau
            self.udic[i] = self.udic[i - 1] + dv_per_dt * 0.001
            print(self.w[i])
            if self.udic[i] > self.u_treshold:
                self.udic[i - 1] = self.spike_value
                self.udic[i] = self.u_reset
                self.spike_times.append(i)

    def cal_w(self, i):
        dw_per_dt = (self.a * (self.udic[i - 1] - self.u_rest) - self.w[i - 1] + self.b * self.tau_w * int(
            1 - np.sign(i - self.spike_times[-1]))) / self.tau_w
        self.w[i] = self.w[i - 1] + 0.001 * dw_per_dt

    def fi(self):
        self.I = {}
        for i in range(0, 5000, 1):
            u = self.u_rest
            t = 1
            a = 1
            w={}
            w[0] = 0
            while u < self.u_treshold:
                dw_per_dt = (self.a * (u - self.u_rest) - w[t - 1] + self.b * self.tau_w * int(
                    1 - np.sign(i - 0))) / self.tau_w
                w[t] = w[t - 1] + 0.001 * dw_per_dt
                dv_per_dt = (-(u - self.u_rest) + self.sharpness * np.exp(
                    (u - self.u_treshold) / self.sharpness) - self.r * w[
                                 t] + self.r * i * 0.001) / self.tau

                u = u + dv_per_dt * 0.001
                t += 1
                if t >= 30000:
                    a = 0
                    break
            if a:
                self.I[i] = 1 / t * 1000
            else:
                self.I[i] = 0
        self.y = np.linspace(0, 5, 1000)
        fig_, ax_ = plt.subplots()
        plt.plot(list(self.I.keys()), list(self.I.values()), label='frecuency')
        plt.ylabel('Hz')
        plt.xlabel('mA')
        plt.title("aelif")
        plt.legend()
        plt.show()
