from constants import synapse,reinforcement
import math


class Synapse:
    def __init__(self,pre,post,weight):
        self.delay = 1
        self.weight = weight
        self.post = post
        self.pre = pre
        self.positive_tau = synapse['positive_tau']
        self.negative_tau = synapse['negative_tau']
        self.positive_weight_dependence = synapse["positive_weight_dependence"]
        self.negative_weight_dependence = synapse["negative_weight_dependence"]
        self.c = reinforcement['c']
        self.tau_c = reinforcement['tau_c']
        self.c_list = list()
        self.weight_list = list()

    def stdp(self,pre,post):
        t_pre = pre.spike_times[-1]
        t_post = post.spike_times[-1]
        if t_post == -1 or t_pre == -1:
            return 0
        delta_t = abs(t_post - t_pre)
        stdp_ = 0
        if t_pre < t_post:
            stdp_ = self.positive_weight_dependence * math.exp(- delta_t / self.positive_tau)
            # self.weight += stdp
        elif t_pre > t_post:
            stdp_ = self.negative_weight_dependence * math.exp(- delta_t / self.negative_tau)
            # self.weight += stdp
        return stdp_

    def calculate_synaptic_tag(self,t):
        d = -self.c/self.tau_c
        b = max(self.alpha(self.post, t), self.alpha(self.pre, t))
        if b:
            a = self.stdp(self.pre, self.post)
            delta_c = d + a * b

        else:
            delta_c= d
        self.c = self.c + delta_c
        self.c = min(0.2,self.c)
        self.c = max(0,self.c)

    def calculate_weight(self,dopamine,t):
        # print('d',dopamine, 'c', self.c)
        delta_w = self.c * dopamine
        self.weight += delta_w
        self.weight = max(self.weight,0.01)
        self.weight = min(self.weight,0.99)
        # if self.post.id == [1,1] and self.pre.id[1]>4 and delta_w != 0:
            # print(delta_w,dopamine,self.c, t,self.post.id,self.pre.id)

    def alpha(self, j, t):
        if t-self.delay in j.spike_times:
            return 1
        else:
            return 0

    def synaptic_change(self,t,d):
        self.calculate_synaptic_tag(t)
        self.calculate_weight(d,t)
        self.c_list.append(self.c)
        self.weight_list.append(self.weight)