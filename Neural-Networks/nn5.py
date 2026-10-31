import numpy as np

# Input Data - 3 Samples with 4 Features each (it means input neurons are 3 but each neuron has 4 features for eg. input neuron are cat,dog,cow features are size,color,weight,sound)
inputs = [
    [1, 2, 3, 2.5],     # Sample 1
    [2.0, 5.0, -1.0, 2.0],  # Sample 2
    [-1.5, 2.7, -3.3, -0.8]  # Sample 3
]

# Weights for Layer 1 - 3 Neurons, each having weights for 4 features
weights1 = [
    [0.2, 0.8, -0.5, 1.0],    # Neuron 1 weights
    [0.5, -0.91, 0.26, -0.5], # Neuron 2 weights
    [-0.26, -0.27, 0.17, 0.87]# Neuron 3 weights
]

# Biases for Layer 1 - One bias per neuron
biases1 = [2, 3, 0.5]

# Calculating Output of Layer 1
# np.dot(weights1, inputs.T) performs matrix multiplication between weights and transposed inputs
# Transposing inputs because shape should be: (neurons x features) dot (features x samples)
layer1_output = np.dot(weights1, np.array(inputs).T) + biases1

print("Output of Layer 1:")
print(layer1_output)

# Weights for Layer 2 - 3 Neurons, taking input from 3 outputs of previous layer
weights2 = [
    [10.1, 0.14, 0.51],    # Neuron 1 weights
    [0.5, 0.12, 0.33],     # Neuron 2 weights
    [10.44, 0.73, 0.13]    # Neuron 3 weights
]

# Biases for Layer 2
biases2 = [1, 2, 0.5]

# Calculating Output of Layer 2
# Again, np.dot(weights2, layer1_output.T) for correct shape multiplication
layer2_output = np.dot(weights2, layer1_output) + biases2

print("Output of Layer 2 (Final Output):")
print(layer2_output)
