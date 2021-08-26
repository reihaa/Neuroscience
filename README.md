# Neuroscience

# phase1:
I simulated LIF, ELIF and adaptive-ELIF nueron models with different kinds of input including arbitrary, fixed and random input, then drew cell's activity during time using different values of parameters. These graphs are included in a report file.

# phase2:
# phase3:
1. I Implemented STDP rule, then measured synaptic weight differences of each pre_synaptic and post_synaptic neurons, included these values in a graph for comparison included in report file, first page.

2. Two neural layers, first layer containing 10 neurons and second layer containing 2 neurons, are simulated. There are synapses between all the first layer neurons and the second layer neurons. At regular intervals, neurons of the first layer spike with two predetermined patterns, and a series of random spikes are performed between these two patterns. The aim is to study the learning of two output layer neurons and the changes in synapic weights using stdp. There are some graphs and outputs in the report showing synaptic weights' defferences and learning patterns of the two output neurons.

# phase4:
1. simulation of the incentive learning law. Then used neural network of the last phase, gave each output neuron a different layer and control their synaptic weights using rewards and punishments (using dopamin concentration). A graph indicating initial weights and final weights of these two neurons is included.

2. A network of 100 neurons, including 80 excitatory neurons and 20 inhibitory neurons is created, including a population of 30 for the input layer and seven populations of 10 for the output layers. The synapses between these neurons are randomly formed, and the weight of the neurons is created randomly for each output layer. A pattern can be selected as the input pattern. In this case, when the neurons in the pattern layer spike after each pattern, amount of dopamine increases, and if the neurons in the other layers spike after the corresponding pattern, the amount of dopamine decreases. Dopamine is a global variable that has the same value throughout the code. The value of synaptic tag and weight for each synapse is calculated as shown in the first part. The number of general neurons, input and output layer neurons, and the possibility of existence a synapse between an input and output layer neurons can be varied. The activity of each layer is calculated and displayed every ten seconds as the average voltage of the neurons in that layer at that time. The graph below indecates the average activity of different populations throughout time.

![unnamed](https://user-images.githubusercontent.com/47301294/131029550-0d409b88-e588-4390-97ae-ab88fd32153d.png)

# phase5:
1. calculated DoG filter matrixes using Gaussian functions for five different sizes. Then projected them on a arbitrary photo using 2D convolution.
2. calculated Gabor filter matrixes for four orientations and 8 sizes. Then projected them on a arbitrary photo.

# phase6:

 
