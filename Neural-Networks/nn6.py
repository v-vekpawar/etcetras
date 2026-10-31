# Object-Oriented Approach for Neural Networks

import numpy as np

# Input Data (X) - 3 Samples, each having 4 Features
X = [
    [1, 2, 3, 2.51],   # Sample 1
    [2.0, 5.0, 1.0, 2.0],  # Sample 2
    [-1.5, 2.7, 3.3, 0.8]  # Sample 3
]

# Class to Create a Dense Layer (Fully Connected Layer)
class LayerDense:
    # Constructor to initialize weights and biases
    def __init__(self, n_inputs, n_neurons):
        # Randomly initializing weights with small values (Gaussian Distribution)
        # Shape of weights: (n_inputs, n_neurons)
        # Multiply by 0.1 to keep values small (helps in stable training)
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        
        # Biases initialized to zero
        # Shape of biases: (1, n_neurons)
        self.biases = np.zeros((1, n_neurons))
        
    # Forward Pass (Matrix Multiplication + Bias Addition)
    def forward(self, inputs):
        # inputs: (number of samples, number of input features)
        # output shape = (number of samples, number of neurons)
        self.output = np.dot(inputs, self.weights) + self.biases


# Creating Layer 1 (First Hidden Layer)
# 4 Inputs because X has 4 features per sample
# 5 Neurons means output from this layer will have 5 features per sample
layer1 = LayerDense(n_inputs=4, n_neurons=5)

# Creating Layer 2 (Second Hidden Layer / Output Layer)
# 5 Inputs because Layer 1 output has 5 features
# 2 Neurons means final output will have 2 features per sample
layer2 = LayerDense(n_inputs=5, n_neurons=2)

# Forward Pass Through Layer 1
layer1.forward(X)
print("Output of Layer 1:")
print(layer1.output)

# Forward Pass Through Layer 2 (Takes Layer 1 Output as Input)
layer2.forward(layer1.output)
print("Output of Layer 2 (Final Output):")
print(layer2.output)
