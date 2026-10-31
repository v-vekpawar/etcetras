"""
2-Layered Neural Network
3-4-3
where 3-Input Neurons, 3-Output Neurons, 4-Hidden Layer Neurons
"""

def neuralNetwork(inputs, weights, biases):
    layer_output = []
    for n_weight,bias in zip(weights,biases):           #zip() converts two lists into pair of tuples into a list
        n_output = 0
        for n_input,weight in zip(inputs,n_weight) :   #for eg. here zip(inputs,n_weight) makes [(2.3,1.1),(1.2,-1.2),(4,1.3)] which is [(inputs[0],weights1[0][0]),(inputs[1],weights1[0][1]),(inputs[2],weights1[0][2])]
            n_output += n_input * weight
        layer_output.append(n_output + bias)
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

# Output layer output
o2 = neuralNetwork(o1, weights2, bias2)

print("Hidden Layer Output:", o1)
print("Final Output:", o2)
