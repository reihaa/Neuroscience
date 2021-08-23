from constants import synapse
import math

class Synapse:
    def __init__(self,pre,post,weight):
        self.delay = 6
        self.weight = weight
        self.post = post
        self.pre = pre
        self.positive_tau = synapse['positive_tau']
        self.negative_tau = synapse['negative_tau']
        self.positive_weight_dependence = synapse["positive_weight_dependence"]
        self.negative_weight_dependence = synapse["negative_weight_dependence"]
        self.time = list()
        self.delta_w_list = list()


    def stdp(self,pre,post):
        t_pre = pre.spike_times[-1]
        t_post = post.spike_times[-1]
        if t_post == -1 or t_pre == -1:
            return

        delta_t = abs(t_post - t_pre)
        if t_pre > t_post:
            delta_w = self.positive_weight_dependence * math.exp(- delta_t / self.positive_tau)
            self.weight += delta_w
        elif t_pre < t_post:
            delta_w = self.negative_weight_dependence * math.exp(- delta_t / self.negative_tau)
            self.weight += delta_w
        #self.time.append((t_post-t_pre))
        #self.delta_w_list.append(delta_w)
        self.weight = max(self.weight,0)
        self.weight = min (self.weight,0.5)

