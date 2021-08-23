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
    "time_": 10000,
    "dt": 1,
    "type": "exitatory",
    "r": 3,
    "tau": 3,
    "u_rest": -0.65,
    "u_threshold": -0.05,
    "sharpness": 0.3,
    "spike_value": 0.7,
    "u_reset": -0.7
}

synapse = {
    'delay' : 0,
    'weight' : 1,
    'positive_tau': 5,
    'negative_tau': 5,
    "positive_weight_dependence":0.0013,
    "negative_weight_dependence" : -0.001
}

model["time"] = int(model["time_"] / model["dt"])

network = {
    'layer_number' : 2,
    'layer_size_list' : [[10,0],[2,1]] #todo
}