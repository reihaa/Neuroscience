# Neuroscience
Neuroscience course, University of Tehran  (Feb - Aug 2020)
# phase1:
I simulated LIF, ELIF and adaptive-ELIF nueron models with different kinds of input including arbitrary, fixed and random input, then drew cell's activity during time using different values of parameters. These graphs are included in a report file.

# phase2:
Simulating population of spiking neurons and measuring it's activities for defferent kinds of input. ( I didn't do this phase seperately but I did it in the next phases)  
# phase3:
1. I Implemented STDP rule, then measured synaptic weight differences of each pre_synaptic and post_synaptic neurons, included these values in a graph for comparison included in report file, first page.

2. Two neural layers, first layer containing 10 neurons and second layer containing 2 neurons, are simulated. There are synapses between all the first layer neurons and the second layer neurons. At regular intervals, neurons of the first layer spike with two predetermined patterns, and a series of random spikes are performed between these two patterns. The aim is to study the learning of two output layer neurons and the changes in synapic weights using stdp. There are some graphs and outputs in the report showing synaptic weights' defferences and learning patterns of the two output neurons.

# phase4:
1. Simulation of the reinforcement learning law. Then used neural network of the last phase, gave each output neuron a different layer and control their synaptic weights using rewards and punishments (using dopamin concentration). A graph indicating initial weights and final weights of these two neurons is included.

2. A network of 100 neurons, including 80 excitatory neurons and 20 inhibitory neurons is created, including a population of 30 for the input layer and seven populations of 10 for the output layers. The synapses between these neurons are randomly formed, and the weight of the neurons is created randomly for each output layer. A pattern can be selected as the input pattern. In this case, when the neurons in the pattern layer spike after each pattern, amount of dopamine increases, and if the neurons in the other layers spike after the corresponding pattern, the amount of dopamine decreases. Dopamine is a global variable that has the same value throughout the code. The value of synaptic tag and weight for each synapse is calculated as shown in the first part. The number of general neurons, input and output layer neurons, and the possibility of existence a synapse between an input and output layer neurons can be varied. The activity of each layer is calculated and displayed every ten seconds as the average voltage of the neurons in that layer at that time. The graph below indecates the average activity of different populations throughout time.

![unnamed](https://user-images.githubusercontent.com/47301294/131029550-0d409b88-e588-4390-97ae-ab88fd32153d.png)

# phase5:
1. calculated DoG filter matrixes using Gaussian functions for five different sizes. Then projected them on a arbitrary photo using 2D convolution.
2. calculated Gabor filter matrixes for four orientations and 8 sizes. Then projected them on a arbitrary photo.

# phase6:
Implementing a computational model based on spiking neural networks for object recognition.

Used BindsNet library. Used on four object groups of CalTech dataset.

The HMAX computational model is implemented using bindsnet.
The model layers consist of:
1. input:
Four different photo sizes. For each size, a gabor filter with a fixed size is applied in four different directions. A total of 16 layers.
2. S1:
Similarly, there are 16 layers that between each layer and its corresponding input layer there is a convolution.
3. C1:
Another 16 layers, each half the size of the previous layers, and there is a MaxPoolConnection between these layers and the s1 layers.
4. S2:
There is a layer multiplied by the number of features of the images that are connected to the previous layer by connection, and the features are extracted from the weight of the synapses between these layers.
5. C2:
There are layers in the number of features multiplied by the size of the photos, which are connected to the previous layer by connection. Features are extracted from the weight of synapses between these layers.
6. And at the end two layers have been added for decision making.
