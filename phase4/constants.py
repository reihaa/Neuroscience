population = {
    "inhibitory_size": 200,
    "exitatory_size": 800,
    "mode": "random",
    "j": 0.1,
    "p": 0.8
}

model = {
    "tau_w": 0.1,
    "a": 3,
    "b": 0.5,
    "current_mode": "random",
    "time": 240,
    "dt": 0.1,
    "1/dt": 10,
    "type": "exitatory",
    "r": 3,
    "tau": 10,
    "u_rest": -0.65,
    "u_threshold": -0.05,
    "sharpness": 0.3,
    "spike_value": 0.7,
    "u_reset": -0.7
}

synapse = {
    'delay' : 0,
    'weight' : 1,
    'positive_tau': 2,
    'negative_tau': 4,
    "positive_weight_dependence":1,
    "negative_weight_dependence" : -1
}

# model["time"] = int(model["time_"] / model["dt"])

network = {
    'layer_number' : 2,
    'layer_size_list' : [[10,0],[2,0]], #todo

}

reinforcement = {
    'dopamine': 0,
    'tau_d': 1,
    'tau_c': 1,
    'da': 0.05,
    'c': 0

}