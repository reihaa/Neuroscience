import random
import math
import matplotlib.pyplot as plt
import numpy as np


class Lif:
    u_rest = -0.65
    u_treshold = -0.05

    def __init__(self, tau, r):
        self.tau = tau
        self.r = r
        self.idic = {}
        self.udic = {}

    def set_tau(self, tau):
        self.tau = tau

    def set_r(self, r):
        self.r = r

    def take_input(self):
        break_points = int(input("how many break points?"))
        j = 0
        pr_bpt = 0
        pr_bpv = 0
        while (j <= 5000):
            for i in range(int(break_points)):
                bpt = int(input())
                bpv = float(input())
                while j <= bpt:
                    self.idic[j] = bpv
                    j += 1

    def random_input(self):
        self.a = random.randint(0, 3)
        self.b = random.randint(0, 100)
        self.c = random.randint(0, 100)
        for i in range(0, 5000, 1):
            self.idic[i] = abs(10 * math.cos(self.b * math.pi / 100000 * i) * math.sin((self.c * math.pi / 100000) * i))

    def fixed_input(self):
        try:
            self.f_inp = float(input())
        except Exception as err:
            print(err)
        for j in range(0, 5000, 1):
            # i = j / 1000
            self.idic[j] = self.f_inp

    def cal_u(self):
        self.udic[0] = self.u_rest
        for i in range(1, 5000, 1):
            self.udic[i] = self.udic[i - 1] - 0.001 / self.tau * (( self.udic[i-1] - self.u_rest) - self.r*self.idic[i])
            if self.udic[i] >= self.u_treshold:
                self.udic[i] = self.u_rest

    def draw(self):
        self.x = np.linspace(0, 5, 1000)
        fig, ax = plt.subplots()
        plt.plot(list(self.idic.keys()), list(self.idic.values()), label='current')
        plt.plot(list(self.udic.keys()), list(self.udic.values()), label='voltage')
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
            while u < self.u_treshold:
                u = u - 0.001 / self.tau * (
                        (u - self.u_rest) - self.r * i * 0.001)
                t += 1
                if t >= 5000:
                    a = 0
                    break
            if a:
                self.I[i] = 1 / t *1000
            else:
                self.I[i] = 0
            print(t)
        self.y = np.linspace(0, 5, 1000)
        fig_, ax_ = plt.subplots()
        plt.plot(list(self.I.keys()), list(self.I.values()), label='current')
        plt.xlabel('mA')
        plt.title("LIF")
        plt.legend()
        plt.show()