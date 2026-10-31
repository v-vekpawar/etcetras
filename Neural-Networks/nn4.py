import numpy as np
def neuralNetwork(inputs, weights, biases):
    layer_output=[]
    for weight, bias in zip(weights, biases):
        neuron_output = np.dot(weight, inputs) + bias
        layer_output.append(neuron_output)
    return layer_output

inputs = [2.3, 1.2, 4]

# 3 inputs → 4 hidden layer neurons
weights1 = [
    [1.1, -1.2, 1.3],
    [-2.1, 2.2, -2.3],
    [3.1, -3.2, 3.3],
    [-4.1, 4.2, -4.3]
]
bias1 = [1, 2, 3, 4]

# 4 hidden neurons → 3 output neurons
weights2 = [
    [1.2, -1.2, 1.3, -1.4],
    [-2.1, 2.2, -2.3, 2.4],
    [3.1, -3.2, 3.1, -3.4]
]
bias2 = [5, 6, 7]

# Hidden layer output
o1 = neuralNetwork(inputs, weights1, bias1)
o1 = [float(i) for i in o1]

# Output layer output
o2 = neuralNetwork(o1, weights2, bias2)
o2 = [float(i) for i in o2]

print("Hidden Layer Output:", o1)
print("Final Output:", o2)
